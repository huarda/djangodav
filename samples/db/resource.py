# Portions (c) 2014, Alexander Klimenko <alex@erix.ru>
# All rights reserved.
#
# Copyright (c) 2011, SmartFile <btimby@smartfile.com>
# All rights reserved.
#
# This file is part of DjangoDav.
#
# DjangoDav is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DjangoDav is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with DjangoDav.  If not, see <http://www.gnu.org/licenses/>.


from django.utils.timezone import now
from djangodav.db.resource import NameLookupDBDavResource
from djangodav.models import CollectionModel, ObjectModel


class MyDBDavResource(NameLookupDBDavResource):
    collection_model = CollectionModel()
    object_model = ObjectModel()

    def write(self, content):
        if not self.exists():
            self.object_model.objects.create(name=self.displayname, parent=self.get_parent().obj)
            return
        self.obj.modified = now()
        self.obj.content = content
        self.obj.save(update_fields=['content', 'modified'])

    def read(self):
        return self.obj.content
