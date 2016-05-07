# encoding:utf-8
import time
from celery.task import task

@task(name='main.tasks._do_kground_work')
# @app.task(name='main.tasks._do_kground_work')
def _do_kground_work(name):
	# 这里用time模拟耗时操作
	for i in range(1, 10):
		print 'hello: %s %s' % (name, i)
		time.sleep(1)

