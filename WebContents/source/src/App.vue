<template>
  <div id="app">
    <div class="base-layer n-type">
      <header-bar />
      <main-contents :articleData="articleData" />
      <footer-menu />
    </div>
  </div>
</template>

<script>
import HeaderBar from './components/HeaderBar'
import MainContents from './components/MainContents'
import FooterMenu from './components/FooterMenu'

const apiUrl = 'https://10lbouggqi.execute-api.ap-northeast-1.amazonaws.com/prd/fuustagram-api'

export default {
  name: 'app',
  components: {
    HeaderBar,
    MainContents,
    FooterMenu
  },
  data () {
    return {
      errorMessage: "",
      articleData: []
    }
  },
  created() {
    if (sessionStorage.getItem('fuustaData') != null){
      this.articleData = JSON.parse(sessionStorage.getItem('fuustaData'))
    } else {
      this.loadArticle()
    }
  },
  methods: {
    popNotification: function() {
      if (document.getElementById('m-notice')) {
        return
      }
      this.errorMessage = "Notification Popup."
      document.body.insertAdjacentHTML("afterbegin",
        '<div id="m-notice" class="n-notify n-center n-notify--fixed">'
        + this.errorMessage
        +'</div>');
    },
    loadArticle: function() {
      let header = {
        "Content-Type": "application/json",
        "X-Api-Key": "qlNVoIKO986yi9cJ1cSSi7fFMObov0dk3EfCAWdJ"
      }
      let parameter = {
        "AppName": "Fuustagram",
        "Action": "GetList"
      }
      this.$axios({
          url: apiUrl,
          method: 'get',
          headers: header,
          params: parameter
        })
        .then(res => {
          console.log(res)
          let articles = []
          let profIconUrl = ''
          res.data.forEach(item =>{
            if (item.post_datetime.startsWith('&')) {
              if (item.post_datetime === '&profile') {
                profIconUrl = item.image_list[0]
              }
            } else {
              let fuustaArticle = {
                'number': item.post_number,
                'text': item.content.join('\n'),
                'imageUrl': item.image_list,
                'tagList': item.hash_tag,
                'datetime': item.post_datetime
              }
              articles.push(fuustaArticle)
            }
          })
          articles.forEach(article => {
            article.profImage = profIconUrl
          })
          articles.sort(function(a,b){
            if(Number(a.number) < Number(b.number)) return -1
            if(Number(a.number) > Number(b.number)) return 1
            return 0})
          
          this.articleData = articles
          sessionStorage['fuustaData'] = JSON.stringify(articles)
        })
        .catch(err => {
          console.log(err.message)
        })
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
  color: #42b983;
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
