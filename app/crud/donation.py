from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User
from app.schemas.donation import DonationCreate


class CRUDDonation(CRUDBase[
    Donation,
    DonationCreate,
    None
]):
    """Класс круд для Donation, унаследованный от CRUDBase."""

    async def get_by_user(
            self,
            session: AsyncSession,
            user: User
    ):
        """Получение пожертования по пользователю."""
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()

    async def get_multi_not_closed(
            self,
            session: AsyncSession
    ) -> List[Donation]:
        """Получение не закрытых пожертований."""
        donations = await session.execute(
            select(self.model.id).where(
                self.model.fully_invested.is_(False)
            )
        )
        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)
