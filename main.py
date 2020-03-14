from common.logger import Log
from common.parse_data import parse_excel_file
import os
from common.tools import root_dir
from common.client import SDKClient

root = root_dir()
datafile = os.path.join(root,'data','data.xlsx')
log = Log()
import json
import pytest

testdata= parse_excel_file(datafile,'API')
print(testdata)
@pytest.mark.parametrize('id,url,method,data,kwargs,excepval',testdata)
def test_cases(id,url,method,data,kwargs,excepval):
    log.info(f'开始进行测试：测试编号为{id},{url},{method},{data},{kwargs},{excepval}')
    try:
        r = SDKClient.do_request(url=url,method=method,data=json.loads(data))
        log.info(f'响应结果为： {json.dumps(r.json())}')
    except AssertionError as e:
        log.error(f'测试失败: 失败信息如下: {e}')
        raise e
    else:
        log.info('测试通过')