from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


# Create logical data abstraction (same as data storage for this first example)
class PersonSchema(Schema):
    class Meta:
        type_ = 'person'
        self_view = 'person_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'person_list'

    id = fields.Str(dump_only=True)
    name = fields.Str(requried=True, load_only=True)
    email = fields.Email(load_only=True)
    birth_date = fields.Date()
    display_name = fields.Function(lambda obj: "{} <{}>".format(obj.name.upper(), obj.email))
    computers = Relationship(self_view='person_computers',
                             self_view_kwargs={'id': '<id>'},
                             related_view='computer_list',
                             related_view_kwargs={'id': '<id>'},
                             many=True,
                             schema='ComputerSchema',
                             type_='computer')


class ComputerSchema(Schema):
    class Meta:
        type_ = 'computer'
        self_view = 'computer_detail'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Str(dump_only=True)
    serial = fields.Str(requried=True)
    owner = Relationship(attribute='person',
                         self_view='computer_person',
                         self_view_kwargs={'id': '<id>'},
                         related_view='person_detail',
                         related_view_kwargs={'computer_id': '<id>'},
                         schema='PersonSchema',
                         type_='person')
