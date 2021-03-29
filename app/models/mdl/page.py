from .hasid import HasidMdl
from typing import Optional
from sqlalchemy import Column, String, DateTime
from pydantic import BaseModel
from fastapi import Query

class PageMdl(HasidMdl):
    __abstract__ = True
    
    # unique要改True, 暂时无用
    link               = Column(String, unique=False,index=True) 
    title              = Column(String(64), index=True)
    content            = Column(String)
    create_date        = Column(DateTime)
    update_date        = Column(DateTime)

    image              = Column(String)
    description        = Column(String(200))
    seo_title          = Column(String(40))
    seo_keywords       = Column(String(256))
    seo_description    = Column(String(400))

class PageOrm(BaseModel):
    link:            Optional[str] = None
    title:           str = Query(...,min_length=1) # 不能为空的意思
    content:         str = Query(...,min_length=1)
    image:           Optional[str] = None
    description:     Optional[str] = None
    seo_title:       str = Query(...,min_length=1)
    seo_keywords:    Optional[str] = None
    seo_description: Optional[str] = None