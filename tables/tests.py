from base.tests.factories import TableFactory


def create_tables(user):
    tables = []
    for i in range(1, 11):
        tables.append(TableFactory(user=user, number=i))
    return tables