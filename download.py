# -*- coding: utf-8 -*-
import oss2
# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAIlE3Wqv2tnZA2', 'MVkoxiAL3TZjLAYk4HGhFtOykVXknn')
# Endpoint以杭州为例，其它Region请按实际情况填写。
endpoint = 'http://oss-cn-beijing.aliyuncs.com'
BucketName = 'areacalculator'
# 设置连接超时时间为30秒。
bucket = oss2.Bucket(auth, endpoint, BucketName, connect_timeout=30, progress_callback=percentage)
