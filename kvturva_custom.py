# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from openerp.osv import osv
from openerp.exceptions import except_orm, Warning, RedirectWarning
import openerp.addons.decimal_precision as dp

from openerp.osv import orm
from openerp.osv import fields

from openerp import tools, exceptions
from openerp.tools.translate import _

from openerp import SUPERUSER_ID


class AccountAnalyticLine(osv.osv):
    _inherit = "account.analytic.line"


    def create(self, cr, uid, vals, context=None):

        task_id = vals['task_id']

        project_task_obj = self.pool.get('project.task').browse(cr, uid, task_id, context=context)

        vals['product_id'] = project_task_obj[0].product_id.id

        return super(AccountAnalyticLine, self).create(cr, uid, vals, context=context)


    def write(self,cr,uid,vals,context=None):

        task_id = vals['task_id']

        project_task_obj = self.pool.get('project.task').browse(cr, uid, task_id, context=context)

        vals['product_id'] = project_task_obj[0].product_id.id

        return super(AccountAnalyticLine, self).write(cr, uid, vals, context=context)
