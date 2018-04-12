from streaming import setting
from streaming.exception import *

def eval_setting_DTP():
	if setting.DTP not in ('D', 'T', 'P'):
		raise ImproperlyConfigured

def eval_setting_MY_NETWORK():
	if setting.MY_NETWORK not in setting.NETWORKS:
		raise ImproperlyConfigured
