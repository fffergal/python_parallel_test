"""
Sample some different methods of parallelising python code.
"""

from argparse import ArgumentParser
from time import sleep
from timeit import default_timer

from gevent.pool import Pool as GPool
from gevent import sleep as gsleep
from multiprocessing import Pool as MPPool
from multiprocessing.dummy import Pool as TPool

POOL_TYPES = dict(gevent=dict(pool=GPool, func=gsleep),
                  multiprocessing=dict(pool=MPPool, func=sleep),
                  threading=dict(pool=TPool, func=sleep),
                  )

parser = ArgumentParser(description=__doc__)
parser.add_argument('sample', choices=POOL_TYPES.keys(),
                    help='Parallelisation method to sample')
parser.add_argument('--items', '-i', type=int, default=100,
                    help='The number of items to iterate over for the sample')
parser.add_argument('--pool', '-p', type=int, default=10,
                    help='The size of the pool (maximum concurrency)')

if __name__ == '__main__':
    args = parser.parse_args()
    conf = POOL_TYPES[args.sample]
    create_start = default_timer()
    iterable = conf['pool'](args.pool).imap(conf['func'], [1] * args.items)
    create_end = default_timer()
    print 'time to make iterable {}s'.format(create_end - create_start)
    for _ in iterable:
        pass
