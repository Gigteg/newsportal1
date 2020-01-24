        $(document).ready(function () {

          //  alert('Привет, Java Script!');

              let valid = true;
              let regExp1 = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
              let regExp2 = ^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])[A-Za-z0-9_\-]{8,16}$
              //let regExp3 = //;

              //Обработчики ввода данных:
              //Ввод логина:
              $('#login').blur(function() {
                      let login = $(this).val();
                      //Проверка регулярки:
                      if (regExp1.test(login)) {
                            //Проверка занятости логина:
                            $.ajax({
                                url:"/account/ajax_reg",
                                data:"login=" + login,
                                success:function(result){
                                    if (result.mess == 'занят'){
                                        $('#login_img').attr('src','../../static/img/cross.png');
                                        $('#login_err').text('Логин занят');
                                        valid = false
                                    } else {
                                        $('#login_img').attr('src','../../static/img/OK.png');
                                        $('#login_err').text('');
                                        valid = true
                                    }

                                   }
                            });

                      } else {
                            $(this).css('border-color','red');
                            $('#login_img').attr('src','../../static/img/cross.png');
                            $('#login_err').text('Логин должен состоять из букв или цифр(6-16) + (_/-)!');
                            valid = false
                      }


              });
                //Ввод пароля:
              $('#pass1').blur(function(){

              })
                //Ввод второго пароля:
              $('#pass2').blur(function(){
              })
                //Ввод имейла:
              $('#email').blur(function(){
              })
                //Исправление данных:
              $('#login').focus(function() {
                    $('#login_err').text('');
              })
              $('#pass1').focus(function() {
                    $('#pass1_err').text('');
              })
              $('#pass2').focus(function() {
                    $('#pass2_err').text('');
              })
              $('#email').focus(function() {
                    $('#email_err').text('');
              });

              // Код проверки результатов валидации:
              //------------------------------------
                //джекуери селектор кнопки сабмит
              $('#submit').clic(function (event) {
              event.preventDefault();
                alert(1);
                if (valid == true) {
                $('#form1').attr('onsubmit', 'return true') // разблокировать отправку данных на сервер
                }else{
                $('#form1').attr('onsubmit', 'return false') // заблокировать отправку данных на сервер
                }
              })

        });
