from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.log import UserLogTable
from app.core.database_engine import db_core
from app.core.module_class import TableModule, ApiModule
from app.core.tools import GetListDepend


class Log(ApiModule, TableModule):
    def get_table(self):
        return [UserLogTable]

    def __init__(self):
        super(Log, self).__init__()

    def _register_api_bp(self, bp: APIRouter):
        """"""

        @bp.get('/user', description='获取用户的logs')
        def get_user_logs(db: Session = Depends(db_core.get_db),
                          ls_depend: GetListDepend = Depends()):
            """"""
            condition = 0
            return ls_depend.get_request(db, UserLogTable, condition)

    def _get_tag(self) -> str:
        """"""
        return 'log'

    def get_module_name(self) -> str:
        return 'log'


log = Log()
