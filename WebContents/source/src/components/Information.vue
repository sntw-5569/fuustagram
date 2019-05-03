<template>
  <div id="information" class="content is-primary">
    <div class="container">
      <h4>Creator Comment</h4>
      <div class="notification main-text">
        fuustagramを閲覧する皆様へ<br>
        <br>
        <br>
        <strong class="title">overture</strong><br>
        fuustagramは、作者が応援してやまない欅坂46のメンバーブログを見て作成するに至りました。<br>
        <br>
        メンバーである齋藤冬優花さんはブログで「fuustagram」という投稿を行なっています。
        欅坂の情報発信はブログか登録制のメッセージアプリが基本なので、他のSNSの利用は行なってません。
        そこで彼女が考えたのがinstagramをブログで表現してしまうという発想です。
        <br>
        ブログのエントリーだけでも十分ですが、せっかくinstagramを模して投稿してくれているので、fuustagramもinstagramっぽく見れたら面白いだろうな…と思いこうして形にしてみました。
        ご本人のブログを見ていただくのが一番の応援効果ですが、こちらのfuustagramも時々見にきてくれたら嬉しく思います。<br>
        <br>
        <br>
        <img class="prof-image" :src="profileImageUrl"><br>
        <a href="http://www.keyakizaka46.com" target="_blank">
        欅坂46公式サイト
        </a><br>
        <br>
        <a href="http://www.keyakizaka46.com/s/k46o/artist/08?ima=0000" target="_blank">
        欅坂46公式 - 齋藤冬優花
        </a><br>
        <br>
        <strong class="title">世界には愛しかない</strong><br>
        欅坂のメディアポリシーがどういったものかはわかりませんが、推察するにweb上で直接ファンと相互交流を取れるのはメッセージアプリやshowroom配信など限定的になっている印象です。instagramのように写真にコメントできる機能も考えましたが、欅坂の運営方針を勝手に察して「ハート」機能だけつけました。皆様の愛のあるハートでこっそりとふーちゃんにリアクションしてみてください。<br>
        <br>
        <strong class="title">危なっかしい計画</strong><br>
        運営会社であるSeed&Flowerさんから「めっ」と言われたら閉鎖します。ファンによる勝手な制作物なので、このサイトで利益を得ようという考えは作者にはありません。純粋に欅坂を知るきっかけや、ファンの皆様のKEYAKILIFEの援助になれば幸いです。<br>
        <br>
        <strong class="title">ここにない足跡</strong><br>
        作者への連絡等はTwitterにてお願いしてます。<br>
        <a href="https://twitter.com/ShinoTatwu" target="_blank">
        <img class="image is-24x24 is-inline-flex twicon" src="https://pbs.twimg.com/profile_images/875170358218735617/qYyASCpq_400x400.jpg">@shinotatwu</a><br>
      </div>
    </div>
    <div class="container"><h5 /></div>
  </div>
</template>

<script>
export default {
  name: 'information',
  props: [
    "profileImageUrl"
  ],
  data () {
    return {
      msg: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  h4 {
    color: #da7518;
    background-color: #ffed1b;
    border-radius: 0 0 50px 50px;
  }
  h5 {
    margin: 0;
    background-color: #ffed1b;
    border-radius: 50px 50px 0 0;
  }
}
.prof-image {
  margin: 3%;
  border-radius: 50%;
  max-width: 180px;
}
.twicon {
  top: 4px;
}
@media screen and (min-width : 300px){
  .main-text {
    font-size: 0.9em;
    strong.title {
      color: #da7518;
      font-size: 1.5em;
    }
  }
}
@media screen and (min-width : 720px){
  .main-text {
    font-size: 1.35em;
    strong.title {
      color: #da7518;
      font-size: 1.5em;
    }
  }
}
</style>
