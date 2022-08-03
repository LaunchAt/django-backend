class ReadOnlyRouter(object):
    def db_for_read(self, *args, **kwargs):
        return 'readonly'

    def db_for_write(self, *args, **kwargs):
        return 'default'

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_migrate(self, *args, **kwargs):
        return True
