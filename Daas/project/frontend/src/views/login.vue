<template>
    <div class="login">
        <div class="user-body-bg"></div>
        <div class="user-login-bg"></div>
        <div class="user-bottom-bg"></div>
        <div class="login-box">
			<img src="../assets/img/icon.png" alt="">
			<form>
				<label class="form-inline">
					<div class="form-inline-font">
						用户名 :
					</div>
					<div class="form-inline-input">
						<input type="text" name="" v-model="username" maxlength="12" placeholder="请输入用户名、邮箱或手机号"/>
					</div>
				</label>
				<label class="form-inline">
					<div class="form-inline-font">
						密码 :
					</div>
					<div class="form-inline-input">
						<input type="password" name="" v-model="password" maxlength="16" placeholder="请输入密码"/>
					</div>
				</label>
				
				<div class="login-btn">
					<div class="user-btn-link">
						<a href="">找回密码？</a>
					</div>
					<span class="join" v-on:click="jumpJoin">注册</span>
					<span v-on:click="login">登录</span>
				</div>
			</form>
		</div>
    </div>
</template>

<script>
import API from "../fetch/api.js";
export default {
	data(){
		return {
			username:'',
			password:'',
		}
	},
	mounted(){
		var self = this;

	},
    methods:{
        jumpJoin(){
			this.$router.push({path:'/join'})
		},
		login(){
			var self=this;
			var options={
				username: self.username,
				password: self.password
			}
			API.login(options).then(res => {
				if(res.success){
					if(res.body.msg == '1'){
						console.log('登录成功！')
						self.$router.push({path:'/'})
					}else{
						alert(res.body.msg)
					}
				}else{
					console.log(res.body)
				}
			})
		}
    }
}
</script>


<style>
body{
	height: 100%;
}
#app{
	height: 100%;
}
.login{
	height: 100%;
	background: url('../assets/img/timg.png') no-repeat;
	background-size: 100% 100%;
}
</style>
<style scoped>
.login-box{
	position: absolute;
	z-index: 9;
    width: 435px;
    top: 48%;
    left: 70%;
    margin-top: -154px;
    margin-left: -205px;
	padding-top: 24px;
    border: 1px solid #777;
    background: #707EA1;
	border-radius: 2px;
	box-shadow: 10px 10px 5px #707EA1;
	color: #fff;
    text-align: center;
}
.login-box form{
	position: relative;
}
.form-inline{
	position: relative;
	display: block;
}
.form-inline + .form-inline{
	margin-top: 10px;
}
.form-inline > div{
	height: 40px;
	line-height: 40px;
}
.form-inline-font{
	position: absolute;
	left: 0;
	width: 110px;
	padding-right: 10px;
	font-family: "Arial";
	font-size: 15px;
	text-align: right;
}
.form-inline-input{
	padding-left: 110px;
}
.form-inline-input input,
.code-box{
	padding: 0 10px;
    width: 300px;
    height: 40px;
    font-size: 14px;
    color: #fff;
    /* text-shadow: 1px 1px 1px black; */
    background: rgba(0, 0, 0, 0.16);
    border: 0;
    border-radius: 5px;
	outline: none;
	box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.3), 0 1px rgba(255, 255, 255, 0.06);
}
.code-box{
	position: relative;
}
.code-box p,
.code-box span{
	display:block;
	position: absolute;
	left: 0;
	height: 40px;
	text-align: center;
	line-height: 40px;
	border-radius: 5px;
}
.code-box span{
	width: 40px;
	background-color:#fff;
	font-family: "宋体";
	font-size: 16px;
	cursor: pointer;
}
.code-box p{
	width: 0;
	background-color: #FFFF99;
	overflow: hidden;
	text-indent: -20px;
	transition: background 1s ease-in;
}
.code-box .code-input{
	display: none;
}
.login-btn{
	padding-right: 25px;
	padding-top: 15px;
	padding-bottom: 10px;
	text-align: right;
	font-size: 0;
}
.user-btn-link{
	display: inline-block;
	vertical-align: sub;
	padding-right: 10px;
}
.user-btn-link a{
	color: #fff;
	font-size: 13px;
}
.user-btn-link a + a{
	margin-left: 5px;
}
.user-btn-link a:hover{
	text-decoration: underline;
}
.login-btn span{
	border: none;
	padding: 8px 12px;
	background-color:#00a1d2;
	border-radius: 3px;
	font-size: 14px;
	color:#fff;
	cursor: pointer;
}
.join{
	margin-right: 10px;
}
.login-btn span:hover{
	box-shadow: 0 0 3px #00a1d2;
	text-shadow: 0 0 1px #b3d6dc,0 0 2px #e6e9de;
}
</style>

