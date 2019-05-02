<template>
<div id="article-panel" class="article-panel">
  <div class="card">
    <header class="card-header is-flex">
      <figure class="profile-icon image is-48x48">
        <img class=" is-rounded" :src="contents.profImage">
      </figure>
      <p class="card-header-title">
        {{ authorName }}
      </p>
    </header>
    <div class="card-image">
      <div class="" v-bind:class="{'n-slider': contents.imageUrl.length > 1 }">
          <figure v-for="(img, index) in contents.imageUrl"
           :key="index" class="image">
            <img :src="img"
              @click="modalControl(img, true)">
          </figure>
      </div>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-left">

        </div>
      </div>
      <div class="content has-text-left">
        <pre class="is-paddingless has-background-white">{{contents.text}}</pre>
        <a class="is-size-7 is-marginless is-block" @click="tagClick(tag)"
          v-for="(tag, index) in contents.tagList" v-bind:key="index">
          #{{tag}}</a>
      </div>
    </div>
    <div class="card-footer">
      <div class="card-footer-item">
        <p class="is-size-7 is-marginless">#{{contents.number}}</p>
      </div>
      <div class="card-footer-item">
        <p class="is-size-7 is-marginless">{{contents.datetime}}</p>
      </div>
      <div class="card-footer-item" 
        :class="{'like-color': !isLiked, 'liked': isLiked}">
          <font-awesome-icon icon="heart" class=" is-size-5" @click="likePush"/>
          <p class="like-count is-size-7" @click="likePush">{{likedCount}}</p>
        </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "article-panel",
  props: [
    "modalControl",
    "contents"
  ],
  data() {
    return {
      authorName: 'fuyuka_saito',
      errorMessage: '',
      canClickLikes: true,
      isLiked: false,
      likedCount: 0,
      isModal: false
    }
  },
  beforeMount() {
    let recordLike = localStorage.getItem(
            this.contents.number + '_lk#' + this.contents.datetime)
    if (recordLike === 'liked') {
      this.isLiked = true
      this.likedCount = Math.max(Number(this.contents.likeCount || 0), 1)
    } else {
      this.likedCount = Number(this.contents.likeCount || '0')
    }
  },
  methods: {
    tagClick: function(tag) {
      let searchBox = document.getElementById('search-input')
      searchBox.value = tag
      if (this.$searchFunction != null) {
        this.$searchFunction({key: 'Enter'}, tag)
      }
      let clearButton = document.getElementById('input-clear')
      if (!'has-text-success'.match(clearButton.attributes.class.value)) {
        let setClass = clearButton.attributes.class.value
        clearButton.setAttribute('class', setClass + ' has-text-success')
      }
    },
    likeInterval: function() {
      this.canClickLikes = true
    },
    likePush: function() {
      if (!this.canClickLikes) {
        return
      } else {
        this.canClickLikes = false
      }

      let keyLike = this.contents.number + '_lk#' + this.contents.datetime
      if (this.isLiked) {
        localStorage.removeItem(keyLike)
        this.isLiked = false
        if (this.likedCount > 0) {
          this.likedCount--
        }
      } else {
        localStorage.setItem(keyLike, 'liked')
        this.isLiked = true
        this.likedCount++
      }
      setTimeout(this.likeInterval, 3000)
      this.sendLikeStatus(this.contents.datetime, this.contents.number)
    },
    sendLikeStatus: function(pkey, nmb) {
      let header = {
        "Content-Type": "application/json",
        "X-Api-Key": "qlNVoIKO986yi9cJ1cSSi7fFMObov0dk3EfCAWdJ"
      }
      let parameter = {
        "AppName": "Fuustagram",
        "Action": "LikeUpdate",
        "LikeState": JSON.stringify({
          "Datetime": pkey,
          "PostNumber": nmb,
          "IsLiked": this.isLiked
        })
      }
      this.$axios({
          url: this.$apiUrl,
          method: 'post',
          headers: header,
          params: parameter
        })
        .then(res => {
          console.log(res)
          this.likedCount = Number(res.data.Likes)
        })
        .catch(err => {
          console.log(err.message)
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.article-panel {
  display: block;
  margin: 10px 0;
}
.card-header-title {
  margin: 0;
}
.profile-icon {
  margin: 5px;
  padding: 5px;
}
.like-color {
  color: #d0d0d0;
  text-shadow: 2px 2px 5px #c58eb0;
}
.liked {
  color: #f9bdf6;
  text-shadow: 2px 2px 5px #c58eb0;
}
.like-count {
  margin: 0 3px;
}
@media screen and (min-width : 300px){
  .card-header-title {
    font-size: 1.15em;
  }
}
@media screen and (min-width : 720px){
  .card-header-title {
    font-size: 1.5em;
  }
}
</style>
