# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/backup_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.mdb.clickhouse.v1 import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_backup__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/clickhouse/v1/backup_service.proto',
  package='yandex.cloud.mdb.clickhouse.v1',
  syntax='proto3',
  serialized_options=_b('ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'),
  serialized_pb=_b('\n3yandex/cloud/mdb/clickhouse/v1/backup_service.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a+yandex/cloud/mdb/clickhouse/v1/backup.proto\x1a\x1dyandex/cloud/validation.proto\"+\n\x10GetBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"s\n\x12ListBackupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"g\n\x13ListBackupsResponse\x12\x37\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32&.yandex.cloud.mdb.clickhouse.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbf\x02\n\rBackupService\x12\x93\x01\n\x03Get\x12\x30.yandex.cloud.mdb.clickhouse.v1.GetBackupRequest\x1a&.yandex.cloud.mdb.clickhouse.v1.Backup\"2\x82\xd3\xe4\x93\x02,\x12*/managed-clickhouse/v1/backups/{backup_id}\x12\x97\x01\n\x04List\x12\x32.yandex.cloud.mdb.clickhouse.v1.ListBackupsRequest\x1a\x33.yandex.cloud.mdb.clickhouse.v1.ListBackupsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/managed-clickhouse/v1/backupsBOZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_backup__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETBACKUPREQUEST = _descriptor.Descriptor(
  name='GetBackupRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.GetBackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backup_id', full_name='yandex.cloud.mdb.clickhouse.v1.GetBackupRequest.backup_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=236,
)


_LISTBACKUPSREQUEST = _descriptor.Descriptor(
  name='ListBackupsRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.ListBackupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.mdb.clickhouse.v1.ListBackupsRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.mdb.clickhouse.v1.ListBackupsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.mdb.clickhouse.v1.ListBackupsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=353,
)


_LISTBACKUPSRESPONSE = _descriptor.Descriptor(
  name='ListBackupsResponse',
  full_name='yandex.cloud.mdb.clickhouse.v1.ListBackupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backups', full_name='yandex.cloud.mdb.clickhouse.v1.ListBackupsResponse.backups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.mdb.clickhouse.v1.ListBackupsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=458,
)

_LISTBACKUPSRESPONSE.fields_by_name['backups'].message_type = yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_backup__pb2._BACKUP
DESCRIPTOR.message_types_by_name['GetBackupRequest'] = _GETBACKUPREQUEST
DESCRIPTOR.message_types_by_name['ListBackupsRequest'] = _LISTBACKUPSREQUEST
DESCRIPTOR.message_types_by_name['ListBackupsResponse'] = _LISTBACKUPSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBackupRequest = _reflection.GeneratedProtocolMessageType('GetBackupRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBACKUPREQUEST,
  __module__ = 'yandex.cloud.mdb.clickhouse.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.GetBackupRequest)
  ))
_sym_db.RegisterMessage(GetBackupRequest)

ListBackupsRequest = _reflection.GeneratedProtocolMessageType('ListBackupsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTBACKUPSREQUEST,
  __module__ = 'yandex.cloud.mdb.clickhouse.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.ListBackupsRequest)
  ))
_sym_db.RegisterMessage(ListBackupsRequest)

ListBackupsResponse = _reflection.GeneratedProtocolMessageType('ListBackupsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTBACKUPSRESPONSE,
  __module__ = 'yandex.cloud.mdb.clickhouse.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.ListBackupsResponse)
  ))
_sym_db.RegisterMessage(ListBackupsResponse)


DESCRIPTOR._options = None
_GETBACKUPREQUEST.fields_by_name['backup_id']._options = None
_LISTBACKUPSREQUEST.fields_by_name['folder_id']._options = None
_LISTBACKUPSREQUEST.fields_by_name['page_size']._options = None
_LISTBACKUPSREQUEST.fields_by_name['page_token']._options = None

_BACKUPSERVICE = _descriptor.ServiceDescriptor(
  name='BackupService',
  full_name='yandex.cloud.mdb.clickhouse.v1.BackupService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=461,
  serialized_end=780,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.mdb.clickhouse.v1.BackupService.Get',
    index=0,
    containing_service=None,
    input_type=_GETBACKUPREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_backup__pb2._BACKUP,
    serialized_options=_b('\202\323\344\223\002,\022*/managed-clickhouse/v1/backups/{backup_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.mdb.clickhouse.v1.BackupService.List',
    index=1,
    containing_service=None,
    input_type=_LISTBACKUPSREQUEST,
    output_type=_LISTBACKUPSRESPONSE,
    serialized_options=_b('\202\323\344\223\002 \022\036/managed-clickhouse/v1/backups'),
  ),
])
_sym_db.RegisterServiceDescriptor(_BACKUPSERVICE)

DESCRIPTOR.services_by_name['BackupService'] = _BACKUPSERVICE

# @@protoc_insertion_point(module_scope)
