<template>
  <div id="app">
    <div class="base-layer n-type">
      <header-bar :searchFunction="articleFilter" :reload="loadArticle" />
      <main-contents :articleData="articleData" />
      <footer-menu />
    </div>
  </div>
</template>

<script>
import HeaderBar from './components/HeaderBar'
import MainContents from './components/MainContents'
import FooterMenu from './components/FooterMenu'
import Vue from 'vue';

export default {
  name: 'app',
  components: {
    HeaderBar,
    MainContents,
    FooterMenu
  },
  data () {
    return {
      articleData: [],
      fullArticleData: []
    }
  },
  created() {
    Vue.prototype.$searchFunction = this.articleFilter
    if (sessionStorage.getItem('fuustaData') != null){
      this.fullArticleData = JSON.parse(sessionStorage.getItem('fuustaData'))
      this.articleData = JSON.parse(sessionStorage.getItem('fuustaData'))
    } else {
      this.loadArticle()
    }
  },
  methods: {
    popNotification: function(msg) {
      if (document.getElementById('m-notice')) {
        return
      }
      document.body.insertAdjacentHTML("afterbegin",
        '<div id="m-notice" class="n-notify n-center n-notify--fixed">'
        + msg
        +'</div>');
    },
    replaceProtocol: function(urlList) {
      let repList = []
      urlList.forEach(url => {
        repList.push(url.replace('http://', 'https://'))
      })
      return repList
    },
    loadArticle: function() {
      this.fullArticleData = []
      this.articleData = []
      let header = {
        "Content-Type": "application/json",
        "X-Api-Key": this.$apiKey
      }
      let parameter = {
        "AppName": "Fuustagram",
        "Action": "GetList"
      }
      this.$axios({
          url: this.$apiUrl,
          method: 'get',
          headers: header,
          params: parameter
        })
        .then(res => {
          let articles = []
          let profIconUrl = ''
          let likeMap = {}
          res.data.forEach(item =>{
            if (item.post_datetime.startsWith('&')) {
              if (item.post_datetime === '&profile') {
                profIconUrl = item.image_list[0].replace('http://', 'https://')
              }
            } else if (item.post_datetime.startsWith('lk#')) {
              let mapKey = item.post_number+'_'+item.post_datetime
              likeMap[mapKey] = item.liked
            } else if (item.post_datetime.startsWith('2')) {
              let imageList = this.replaceProtocol(item.image_list)          
              let fuustaArticle = {
                'number': item.post_number,
                'text': item.content.join('\n'),
                'imageUrl': imageList,
                'tagList': item.hash_tag,
                'datetime': item.post_datetime
              }
              articles.push(fuustaArticle)
            }
          })
          articles.forEach(article => {
            article.profImage = profIconUrl
            let mapKey = article.number+'_lk#'+article.datetime
            article.likeCount = likeMap[mapKey] || 0
          })
          articles.sort(function(a,b){
            if(Number(a.number) < Number(b.number)) return -1
            if(Number(a.number) > Number(b.number)) return 1
            return 0})
          
          this.articleData = articles
          this.fullArticleData = [].concat(articles)
          sessionStorage['fuustaData'] = JSON.stringify(articles)
        })
        .catch(err => {
          console.log(err.message)
        })
    },
    articleFilter: function(event, keyword) {
      if (event.key === 'Backspace' && keyword === '') {
        this.articleData = [].concat(this.fullArticleData)
        return
      }
      if (event.key != 'Enter' || keyword.trim() === '') {
        return
      }
      let hitArticle = []
      let keys = keyword.replace(/　/gi, ' ').split(' ')

      this.fullArticleData.forEach(article => {
        let hit = false
        keys.forEach(key => {
          article.tagList.forEach(tag => {
            if (tag.match(key)) {
              hit = true
            } else if (tag === key) {
              hit = true
            }
          })
          if (!hit && article.text.match(key)) {
            hit = true
          }
          if (hit && hitArticle.indexOf(article) === -1) {
            hitArticle.push(article)
          }
        })
      })
      
      this.articleData = hitArticle
      if (this.articleData.length === 0) {
        this.popNotification('Not found result for search.')
      }
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma/bulma.sass';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #0a7042;
}
.n-notify.n-notify--fixed {
  z-index: 70;
}
.n-slider--arrow, .n-slider--nav a {
  --control-bg: rgba(255, 255, 255, 0.308);
	--control-color: rgb(7, 211, 48);		
	--control-active-bg: #7be289ad;
	--control-active-color: rgb(240, 231, 231);
	--control-highlight: #27ee8a;
}

.base-layer {
  position: relative;
}
.n-notify {
  height: 80px;
}

.-no-disp {
  display: none;
}
.-inline {
  display: inline;
}
</style>
