from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound
from sqlalchemy.orm.exc import NoResultFound

from api.schemas import PersonSchema, ComputerSchema
from database import db
from database.models import Computer, Person


# Create resource managers
class PersonList(ResourceList):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}


class PersonDetail(ResourceDetail):
    def before_get_object(self, view_kwargs):
        if view_kwargs.get('computer_id') is not None:
            try:
                computer = self.session.query(Computer).filter_by(id=view_kwargs['computer_id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'computer_id'},
                                     "Computer: {} not found".format(view_kwargs['computer_id']))
            else:
                if computer.person is not None:
                    view_kwargs['id'] = computer.person.id
                else:
                    view_kwargs['id'] = None

    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person,
                  'methods': {'before_get_object': before_get_object}}


class PersonRelationship(ResourceRelationship):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}


class ComputerList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(Computer)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Person).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Person: {} not found".format(view_kwargs['id']))
            else:
                query_ = query_.join(Person).filter(Person.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            person = self.session.query(Person).filter_by(id=view_kwargs['id']).one()
            data['person_id'] = person.id

    schema = ComputerSchema
    data_layer = {'session': db.session,
                  'model': Computer,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}


class ComputerDetail(ResourceDetail):
    schema = ComputerSchema
    data_layer = {'session': db.session,
                  'model': Computer}


class ComputerRelationship(ResourceRelationship):
    schema = ComputerSchema
    data_layer = {'session': db.session,
                  'model': Computer}
