# WPS
### WPS微信小程序邀请(无签到，无提醒)<br>
### 使用方法<br>
Github Actions版本(因Secrets内容会被Actions屏蔽，所以Actions看不见用户id)<br>
1.点击项目右上角的Fork，Fork此项目<br>
2.到自己Fork的项目点击Setting→Secrets→New secrets<br>
3.Name填写wps_userid，Value填写 需要邀请的用户id(多用户回车分隔)<br>
4.在"Actions"中的"run"下点击"Run workflow"即可手动执行<br>
<br>
<br>
[腾讯云函数SCF](https://console.cloud.tencent.com/scf/index)的版本<br>
1.下载requirements.zip所需库，到[层](https://console.cloud.tencent.com/scf/layer)里面新建一个层<br>
2.到[函数服务](https://console.cloud.tencent.com/scf/list)里面新建一个函数，输入名字，运行环境选择python3.6，选择空白模板，下一步<br>
3.修改执行方法为index.main，修改index.py文件，把SCF版py文件内容覆盖掉里面的函数<br>
4.高级设置，添加多个环境变量key内输入：wps_userid，value内输入需要邀请的用户id(多用户\n分隔)<br>
5.层配置，添加层，选择刚才新建的层。最后点完成<br>
6.进入函数→触发管理→新建触发器，按自己需求定时启动<br>