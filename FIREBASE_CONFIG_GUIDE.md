# Firebase配置与降级方案指南

## 问题分析

您遇到的 `auth/invalid-api-key` 错误通常表示Firebase初始化时使用了无效的API密钥。根据代码分析，当前应用尝试从未定义的变量中获取Firebase配置。

## 一、获取正确的Firebase v9配置

### 步骤1：访问Firebase控制台
1. 打开 [Firebase控制台](https://console.firebase.google.com/)
2. 登录您的Google账号
3. 点击 "添加项目" 或选择现有项目

### 步骤2：获取配置信息
1. 在项目概览页面，点击齿轮图标 ⚙️，选择 "项目设置"
2. 向下滚动到 "您的应用" 部分
3. 如果没有Web应用，请点击 "</>" 图标添加
4. 输入应用昵称（如 "女帝启示录"），勾选 "也将Firebase Hosting用于此应用"（可选）
5. 点击 "注册应用"
6. 在配置代码中，您将看到类似这样的配置对象：

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyBxZ77VtT7C4LxZ1H3Z8X7Y9W0V6U5I4O3",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-12345",
  storageBucket: "your-project-12345.appspot.com",
  messagingSenderId: "987654321098",
  appId: "1:987654321098:web:abcdef1234567890abcdef"
};
```

### 步骤3：启用匿名认证（如果需要）
1. 在项目设置页面，点击左侧菜单的 "构建" > "认证"
2. 点击 "开始使用"
3. 选择 "匿名" 提供商
4. 点击右上角 "启用"

## 二、降级开发方案说明

我已经为您实现了一个降级开发方案，具有以下特点：

1. **自动检测无效配置**：当检测到无效API密钥时，自动切换到开发模式
2. **本地存储模拟**：使用localStorage保存起居注数据，无需Firebase连接
3. **完整UI功能**：所有界面功能（番茄钟、设置、起居注）都能正常使用
4. **错误恢复**：即使Firebase初始化失败，也会在2秒后自动降级到开发模式

### 使用方法

降级方案已经内置在代码中，您可以：

1. **直接运行**：打开index.html，当Firebase配置无效时会自动进入开发模式
2. **测试功能**：在开发模式下，您可以完全测试应用的UI和功能
3. **查看日志**：控制台会显示 "开发模式：使用模拟数据进行开发" 的信息

### 数据保存

在开发模式下：
- 起居注会保存在浏览器的localStorage中
- 数据以 `dev_daily_log` 键存储
- 刷新页面后数据依然保留

## 三、恢复正式Firebase配置

当您获取到正确的Firebase配置后，可以通过以下方式更新：

### 方法1：直接修改代码（推荐用于测试）

1. 编辑index.html文件
2. 找到以下代码段：

```javascript
const firebaseConfig = JSON.parse(typeof __firebase_config !== 'undefined' ? __firebase_config : JSON.stringify({
    apiKey: "YOUR_API_KEY",
    authDomain: "your-project.firebaseapp.com",
    projectId: "your-project",
    storageBucket: "your-project.appspot.com",
    messagingSenderId: "123456789012",
    appId: "1:123456789012:web:123456789abcdef"
}));
```

3. 将示例值替换为您从Firebase控制台获取的实际配置

### 方法2：通过环境变量（推荐用于生产）

如果您使用的是支持环境变量的部署环境，可以在部署前设置 `__firebase_config` 变量为您的Firebase配置JSON字符串。

## 四、注意事项

1. **安全提示**：确保不要在公共代码仓库中提交实际的Firebase API密钥
2. **开发与生产**：降级方案仅用于开发测试，生产环境请使用有效的Firebase配置
3. **数据迁移**：开发模式下保存的数据不会同步到Firebase，请注意数据迁移
4. **功能限制**：开发模式下不支持用户认证、多设备同步等Firebase特有功能

## 五、常见问题排查

1. **配置无效**：确认您的配置对象格式正确，API密钥无误
2. **认证失败**：确认已在Firebase控制台启用了相应的认证提供商
3. **存储错误**：检查项目是否启用了Firestore数据库
4. **跨域问题**：本地开发时可能遇到跨域问题，可尝试使用Chrome扩展或本地服务器

---

祝您开发顺利！如有任何问题，请随时查阅Firebase官方文档或在此项目中寻求帮助。