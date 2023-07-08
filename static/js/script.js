        // 获取图像上传控件和预览容器
        const imageUpload = document.getElementById('imageUpload');
        const currentImages = document.getElementById('currentImages');
        const imagePreview = document.getElementById('imagePreview');

        // 设置最大预览图像数量
        const maxPreviewImages = 15;

        // 监听图像上传控件的change事件
        imageUpload.addEventListener('change', function (event) {
            // 清空预览容器
            imagePreview.innerHTML = '';
            currentImages.innerHTML = ''; // 清空当前上传的图像栏目
            // 遍历选择的文件
            for (let i = 0; i < event.target.files.length; i++) {
                if (i >= maxPreviewImages) {
                    break; // 达到最大预览数量，停止添加新的预览图像
                }
                const file = event.target.files[i];

                // 创建图像预览元素
                const img = document.createElement('img');
                img.classList.add('preview-image');
                img.src = URL.createObjectURL(file);

                // 创建图像容器并将图像预览元素添加到容器中
                const imgContainer = document.createElement('div');
                imgContainer.classList.add('image-container');
                imgContainer.appendChild(img);

                // 将图像容器添加到预览容器中
                currentImages.appendChild(imgContainer); // 添加到当前上传的图像栏目
            }
        });


        // --
        // 获取审核进度提示元素
        const progressMessage = document.getElementById('progressMessage');

        // 监听提交按钮的点击事件
          const submitButton = document.querySelector('input[type="submit"]');
          submitButton.addEventListener('click', function () {
            // 检查是否选择了图像文件
            if (imageUpload.files.length === 0) {
              return; // 如果没有选择图像文件，则不显示审核进度提示
            }

            // 显示审核进度提示
            progressMessage.style.display = 'block';
          });

        // 审核完成后隐藏审核进度提示
        // 在合适的位置调用以下代码
        progressMessage.style.display = 'none';
        // 获取审核进度提示元素和显示省略号的<span>元素
        const dotsElement = document.getElementById('dots');

        // 定义一个计数器变量，用于控制省略号的个数
        let dotsCount = 0;

        // 定义一个函数，用于更新省略号的显示
        function updateDots() {
          dotsCount = (dotsCount + 1) % 5; // 循环计数，取值范围为 0~4

          // 根据计数器的值设置省略号的个数
          let dots = '';
          for (let i = 0; i < dotsCount; i++) {
            dots += '.';
          }

          // 更新<span>元素的内容
          dotsElement.textContent = dots;
        }

        // 使用定时器每隔一秒更新省略号的显示
        setInterval(updateDots, 1000);



        // ===
         // 获取当前时间的函数
        // 获取当前日期和时间
        function getCurrentDateTime() {
            var now = new Date();
            var date = now.toLocaleDateString();
            var time = now.toLocaleTimeString();
            return date + ' ' + time;
        }

        // 在元素中显示当前日期和时间
        function displayCurrentDateTime() {
            var currentDateTime = document.getElementById('currentDateTime');
            currentDateTime.textContent = getCurrentDateTime();
        }

        // 页面加载完成时调用显示当前日期和时间的函数
        setInterval(displayCurrentDateTime,1000)