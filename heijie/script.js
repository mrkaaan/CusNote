// 获取容器
const articleContainer = document.querySelector('.article');

// 从 JSON 文件中读取歌词数据
fetch('heijie.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to load the JSON file');
        }
        return response.json();
    })
    .then(data => {
        // 提取第一句歌词并弹出
        // const firstSentence = data.lyrics[0];
        // const firstSentenceText = firstSentence.map(word => word.text).join('');
        // alert(`第一句歌词: ${firstSentenceText}`);
        renderLyrics(data.lyrics); // 从 data.lyrics 中读取歌词数据
    })
    .catch(error => {
        console.error('Error:', error);
        articleContainer.innerHTML = '<p>Failed to load lyrics. Please check the JSON file.</p>';
    });

// 渲染歌词
function renderLyrics(lyrics) {
    lyrics.forEach(sentence => {
        const passageDiv = document.createElement('div');
        passageDiv.classList.add('passage');

        sentence.forEach(word => {
            const rubyElement = document.createElement('ruby');
            rubyElement.classList.add('word');

            const rbElement = document.createElement('rb');
            rbElement.textContent = word.text;

            const rpOpen = document.createElement('rp');
            rpOpen.textContent = '（';

            const rtElement = document.createElement('rt');
            rtElement.textContent = word.pronunciation;

            const rpClose = document.createElement('rp');
            rpClose.textContent = '）';

            rubyElement.appendChild(rbElement);
            rubyElement.appendChild(rpOpen);
            rubyElement.appendChild(rtElement);
            rubyElement.appendChild(rpClose);

            if (word.text === "，" || word.text === "。") {
                const spanElement = document.createElement('span');
                spanElement.classList.add('point');
                spanElement.textContent = word.text;
                passageDiv.appendChild(spanElement);
            } else if (word.text === "(" || word.text === ")") {
                const spanElement = document.createElement('span');
                spanElement.classList.add('symbol');
                spanElement.textContent = word.text;
                passageDiv.appendChild(spanElement);
            } else {
                passageDiv.appendChild(rubyElement);
            }
        });

        articleContainer.appendChild(passageDiv);
    });
}