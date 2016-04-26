#! /usr/bin/env python
# encoding: utf-8

def options(opt):
	opt.load('compiler_c')

def configure(conf):
	conf.load('ar')
	conf.load('compiler_c')
	if 'LIB_PTHREAD' not in conf.env:
		conf.check_cc(lib = 'pthread')

	conf.env.append_value('CFLAGS', '-O3')
	conf.env.append_value('CFLAGS', '-std=c99')
	conf.env.append_value('CFLAGS', '-march=native')

	conf.env.append_value('LIB_PTASK', conf.env.LIB_PTHREAD)
	conf.env.append_value('OBJ_PTASK', ['queue.o', 'queue_internal.o', 'ptask.o'])

def build(bld):

	bld.objects(source = 'queue.c', target = 'queue.o')
	bld.objects(source = 'queue_internal.c', target = 'queue_internal.o')
	bld.objects(source = 'ptask.c', target = 'ptask.o')

	bld.stlib(
		source = ['unittest.c'],
		target = 'ptask',
		use = bld.env.OBJ_PTASK,
		lib = bld.env.LIB_PTASK)

	bld.program(
		source = ['unittest.c'],
		target = 'unittest',
		use = bld.env.OBJ_PTASK,
		lib = bld.env.LIB_PTASK,
		defines = ['TEST'])
