<?php
if(!isset($_GET['lang']))
Header("Location: /?lang=zh-cn");
?>

<html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="https://cdn.bootcss.com/element-ui/2.13.1/theme-chalk/index.css">
</head>

<body>

    <div id="app">

    <el-row style="margin:50px">
        <el-col span='12' :offset='6'>

        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>欢迎</span>
                <el-link href="/?lang=en-us"> English </el-link>
                <el-link href="/?lang=zh-cn"> 中文 </el-link>
            </div>
            <p>


            <?php

                @extract($_GET);

                if($lang == 'zh-cn')
                    $language_file = 'zh-cn.txt';
                else if($lang == 'en-us')
                    $language_file = 'en-us.txt';

                echo file_get_contents($language_file);

                ?>


            </p>
        </el-card>
        </el-col>
    </el-row>

    

    </div>

</body>
<script src="https://cdn.bootcss.com/vue/2.6.11/vue.js"></script>
<script src="https://cdn.bootcss.com/element-ui/2.13.1/index.js"></script>
<script>
    new Vue({
      el: '#app',
      data: function() {
        return { visible: false }
      }
    })
  </script>
</html>