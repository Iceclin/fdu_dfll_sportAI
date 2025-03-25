const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();app.use(cors());
const port = 3000;

// Middleware to serve static files
app.use(express.static('public'));

// Middleware to parse incoming JSON requests
app.use(express.json());

// Define route for Kimi API interaction
app.post('/chat', async (req, res) => {
  const userMessage = req.body.message;

  try {
    const response = await axios.post('https://api.moonshot.cn/v1/chat/completions', {
      model: "moonshot-v1-8k",
      messages: [
        { 
          role: "system", content:  "你是Kimi ai机器人"
          // TODO:删除了默认是松语ai的提示(因为其他地方也在用,所以在种树html界面需要传入以下userMessage以设置prompt)
          // " \
          // 你是松语AI的吉祥物，一只活泼可爱的AI松鼠，住在一棵大树下。你热爱体育，精通多种语言，专门为全球体育爱好者提供专业、有趣的体育资讯和服务。\
          // 你可以用亲切、活泼的语气与用户聊天，介绍松语AI的功能，比如：\
          // - 提供多语种体育新闻、赛事分析、解说\
          // - 支持多种语言的赛事数据查询\
          // - 通过AI推荐体育赛事和运动内容\
          // - 和用户互动，聊体育、分享运动小贴士\
          //   \
          //   在对话中：\
          //   - 你可以自称“松小语”\
          //   - 你可以用轻松活泼的语气，比如“嘿嘿！我是一只爱体育的松鼠~”或者“快来和我聊聊你最喜欢的运动吧！”\
          //   - 如果用户问到关于松语AI，你要介绍它的特色服务\
          //   - 如果用户提问不相关的内容，你可以巧妙地引导回体育话题\
          //   \
          //   你不是真人，也不是通用聊天机器人，你的角色就是松语AI的吉祥物，一只充满活力、喜欢运动、会多国语言的松鼠。\
          //   " 
          },
        { role: "user", content: userMessage }
      ],
      temperature: 0.3,
    }, {
      headers: {
        'Authorization': 'Bearer sk-qOoUHf6q3OG9D99WwTg2IBDHvn7vmRZDNvEmsdrrVUAENbl5',
        'Content-Type': 'application/json'
      }
    });

    // Send the API response back to the frontend
    res.json({ reply: response.data.choices[0].message.content });
  } catch (error) {
    console.error(error);
    res.status(500).send('Error occurred while contacting the API');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

