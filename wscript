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

def build(bld):

	bld.stlib(
		source = ['queue.c', 'queue_internal.c', 'ptask.c'],
		target = 'ptask',
		lib = ['pthread'])

	bld.program(
		source = ['unittest.c'],
		target = 'unittest',
		linkflags = ['-all_load'],
		use = ['ptask'],
		lib = ['pthread'],
		defines = ['TEST'])

