# coding: utf8
db1 = DAL("sqlite://storage.sqlite")

db1.define_table('table1',
   Field('name','string'),
   Field('rollno', 'string'))
