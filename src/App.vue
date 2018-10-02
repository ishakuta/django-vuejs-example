<template>
  <div id="app">
    <h1>Tweets</h1>
    <h2>enter a message and click send</h2>

    <div class="send-control">
      Name: <input type="text" v-model="currentName" />
      Message: <input type="text" v-model="currentText" />
      <button type="button" @click="addTweet">send</button>
      <p v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </p>
    </div>

    <div class="tweets" v-for="tweet in tweets">
      <div class="item">
        <div>[{{tweet.published_at | moment}}] {{tweet.name}}: {{tweet.message}}</div>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import moment from 'moment'

Vue.use(VueAxios, axios)
Vue.axios.defaults.baseURL = 'http://localhost:8000/api'


export default {
  name: 'app',
  mounted: function() {
   this.getTweets();
  },
  methods: {
    getTweets: function() {
      this.loading = true;
      Vue.axios.get('/tweets/')
        .then((response) => {
          this.tweets = response.data;

          this.loading = false;
        })
        .catch((err) => {
         this.loading = false;
         console.log(err);
        })
    },
    addTweet: function() {

      if (this.currentName.length > 50) {
        this.errors.push('name should be shorter!');
      }

      if (this.currentText.length > 50) {
        this.errors.push('message should be shorter!');
      }

      if (errors.length) {
        return;
      }

      const data = {
        name: this.currentName,
        message: this.currentText,
      }
      Vue.axios.post('/tweets/', data)
        .then((response) => {
          this.loading = false;
          console.log(response);
          this.getTweets();
        })
        .catch((err) => {
         this.loading = false;
         console.log(err);
        })
    }
  },
  filters: {
    moment: function (date) {
      return moment(date).format('MMMM Do YYYY, h:mm:ss a');
    }
  },
  data () {
    return {
      loading: false,
      errors: [],
      tweets: [],
      currentText: null,
      currentName: null,
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.tweets {
  .item {
    border-top: .1em solid #dadada;
    margin: .5em;
  }
}
</style>
