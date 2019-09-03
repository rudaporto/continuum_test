from trips.models import Trip, Session


def create_trip(payload):
    session = Session()
    trip = Trip(payload=payload)
    session.add(trip)
    session.commit()
    return trip


def update_trip(uid, payload):
    session = Session()
    trip = session.query(Trip).get(uid)
    trip.payload = payload
    session.commit()
    return trip


def print_versions(versions):
    for item in versions:
        print(item.id, item.payload)
    print()


def main():
    payload = {
        'foo': 'a',
        'bar': 'b',
    }
    t1 = create_trip(payload)
    all_versions1 = t1.versions.all()
    print('Versions after insert:')
    print_versions(all_versions1)

    payload['foo'] = 'c'
    t1 = update_trip(t1.id, payload)
    all_versions2 = t1.versions.all()
    print('Versions after first update:')
    print_versions(all_versions2)

    print('Versions after second update (with no change):')
    t1 = update_trip(t1.id, payload)
    all_versions3 = t1.versions.all()
    print_versions(all_versions3)

    payload['bar'] = 'z'
    print('Versions after third update (with change):')
    t1 = update_trip(t1.id, payload)
    all_versions3 = t1.versions.all()
    print_versions(all_versions3)


if __name__ == '__main__':
    main()
