from datetime import datetime as dt

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import ModelType, CRUD_TYPE


def close_model(model: ModelType) -> ModelType:
    """Функция закрытия модели."""
    model.invested_amount = model.full_amount
    model.fully_invested = True
    model.close_date = dt.utcnow()
    return model


async def invest(
        investment_id: int,
        investment_crud: CRUD_TYPE,
        target_crud: CRUD_TYPE,
        session: AsyncSession,
) -> ModelType:
    """Корутина инверстирования"""
    investments = await investment_crud.get_multi_not_closed(session)

    target_object = await target_crud.get(investment_id, session)
    remaining_amount = target_object.full_amount - target_object.invested_amount
    remainder = 0

    for investment_obj_id in investments:
        investment_object = await investment_crud.get(investment_obj_id, session)
        remainder = investment_object.full_amount - investment_object.invested_amount

        if remainder > remaining_amount:
            investment_object.invested_amount += remaining_amount
            target_object = close_model(target_object)
            session.add(investment_object)
            break
        else:
            remaining_amount -= remainder
            investment_object = close_model(investment_object)
            session.add(investment_object)

    if remaining_amount == 0:
        target_object = close_model(target_object)
    elif remaining_amount > 0 and investments:
        target_object.invested_amount += remaining_amount

    session.add(target_object)
    await session.commit()
    await session.refresh(target_object)

    return target_object
