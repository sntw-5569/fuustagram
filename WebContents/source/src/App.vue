<template>
  <div id="app">
    <div class="base-layer n-type">
      <header-bar />
      <main-contents />
      <button @click="dummyPush()">Push Me.</button>
      <footer-menu />
    </div>
  </div>
</template>

<script>
import HeaderBar from './components/HeaderBar'
import MainContents from './components/MainContents'
import FooterMenu from './components/FooterMenu'

export default {
  name: 'app',
  components: {
    HeaderBar,
    MainContents,
    FooterMenu
  },
  data () {
    return {
      errorMessage: ""
    }
  },
  methods: {
    dummyPush: function() {
      if (document.getElementById('m-notice')) {
        return
      }
      this.errorMessage = "Notification Popup."
      document.body.insertAdjacentHTML("afterbegin",
        '<div id="m-notice" class="n-notify n-center n-notify--fixed">'
        + this.errorMessage
        +'</div>');
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
