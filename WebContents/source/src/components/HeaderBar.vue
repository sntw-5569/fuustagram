<template>
  <header class="header-bar">
    <nav class="level is-flex">
      <div class="level-left title-logo">
        <figure class="image is-4by1">
          <a href="/" class="is-inline">
            <img :src="logo" href="/">
          </a>
        </figure>
      </div>
      <div class="level-right is-flex">
        <div class="level-item control has-icons-left">
          <input id="search-input" class="input search-input"
            type="text" placeholder="keyword" v-on:input="inputTextSync($event)"
            v-on:keydown="searchFunction($event, $event.srcElement.value)">
          <span class="icon is-small is-left input-innner">
            <font-awesome-icon icon="search" class="input-innner-icon"/>
          </span>
        </div>
        <div class="level-item">
          <span class="icon is-small input-reset" @click="inputClear()">
            <font-awesome-icon id="input-clear" icon="times" class="input-innner-icon"
              :class="{'has-text-success': keyword != ''}" />
          </span>
        </div>
        <div class="level-item head-icon">
          <a class="is-marginless" @click="inputClear(); reload();">
            <font-awesome-icon icon="sync-alt"/>
          </a>
        </div>
        <div class="level-item head-icon">
          <a class="is-marginless" @click="scroolReset()">
            <font-awesome-icon icon="arrow-alt-circle-up" />
          </a>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import appLogo from '../assets/fuusta_logo.png'

export default {
  name: "haeder-bar",
  props: [
    "searchFunction",
    "reload"
  ],
  data() {
    return {
      keyword: '',
      logo: appLogo
    }
  },
  methods: {
    inputTextSync: function(event) {
      this.keyword = event.srcElement.value
    },
    inputClear: function() {
      document.getElementById('search-input').value = ''
      this.keyword = ''
      if (this.$searchFunction != null) {
        this.$searchFunction({key: 'Backspace'}, '')
      }
      let target = document.getElementById('input-clear')
      let setClass = target.attributes.class.value.replace('has-text-success', '')
      target.setAttribute('class', setClass)
    },
    scroolReset: function() {
      window.scrollTo(0, 0)
    }
  }
}
</script>

<style lang="scss" scoped>
.header-bar {
  position: fixed;
  top: 0;
  overflow: hidden;
  background-color: white;
  // border-bottom: solid 1px rgb(150, 150, 150);
  box-shadow: 1px 2px 3px 0px #bbb;
  z-index: 50;
}
@supports (position: sticky) {
  .header-bar {
    position: sticky;
  }
}
@supports (position: -webkit-sticky) {
  .header-bar {
    position: -webkit-sticky;
  }
}

.level-item {
  margin: 0;
}
.input {
    color: darkred;
    background-color: rgb(238, 238, 238);
    font-size: small;
}
.input-innner-icon {
  color: slategray;
}
.input-reset {
  position: relative;
}

@media screen and (min-width : 300px){
  nav.level {
    padding: 0;
    margin: 0;
  }
  .level-right {
    width: 60%;
    margin: 0;
    div {
      padding: 2px;
    }
  }
  .input {
    width: 100%;
  }
  div.control {
    width: 80%;
  }

  .title-logo {
    width: 30%;
    img {
      width: 100%;
    }
  }
  .head-icon {
    font-size: 22px;
  }
}

@media screen and (min-width : 720px){
  div.level-right {
    padding-top: 5px;
  }
  .title-logo {
    width: 30%;
    max-width: 200px
    img {
      width: 100%;
      margin: 10px;
    }
  }
  .head-icon {
    font-size: 35px;
  }
  .level-right {
    width: 60%;
    margin: 0;
    div {
      padding: 2px;
    }
  }
  .input {
    width: 100%;
  }
  div.control {
    width: 80%;
  }
}

</style>
