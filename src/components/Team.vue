<template>
    <div>
      <v-container >
        <p class="pa-5 mt-10 text-h5 font-weight-medium text-uppercase text-center">Core Team</p>
        <v-row>
          <v-col cols="12" sm="12" md="4" v-for="(member, index) in core" :key="index">
            <v-card width="250" class="rounded-xl mx-auto">
                <div class="text-center">
                  <v-avatar size="120" class="mt-5">
                    <v-img :src="member.get_image"></v-img>
                  </v-avatar>
                </div>
                <span class="text-h5 text-center font-weight-bold d-block mt-5">{{ member.name }}</span>
                <span class="text-center d-block">{{ member.title }}</span>
                <div class="d-flex justify-space-around pa-5">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <a @click="mailTo(member.email)" v-bind="attrs" v-on="on" style="text-decoration:none; color:white">
                        <v-icon size="25" class="text--lighten-1">mdi-gmail</v-icon>
                      </a>
                    </template>
                    <span>{{ member.email }}</span>
                  </v-tooltip>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <a :href="member.linkedin" v-bind="attrs" v-on="on" target="_blank" style="text-decoration:none; color:white">
                        <v-icon size="25" class="text--lighten-1">mdi-linkedin</v-icon>
                      </a>
                    </template>
                    <span>{{ member.linkedin }}</span>
                  </v-tooltip>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <a :href="member.portfolio" v-bind="attrs" v-on="on" target="_blank" style="text-decoration:none; color:white">
                        <v-icon size="25" class="text--lighten-1">mdi-web</v-icon>
                      </a>
                    </template>
                    <span>{{ member.portfolio }}</span>
                  </v-tooltip>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <a :href="member.github" v-bind="attrs" v-on="on" target="_blank" style="text-decoration:none; color:white">
                        <v-icon size="25" class="text--lighten-1">mdi-github</v-icon>
                      </a>
                    </template>
                    <span>{{ member.github }}</span>
                  </v-tooltip>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <a href="#" v-bind="attrs" v-on="on" style="text-decoration:none; color:white">
                        <v-icon size="25" class="text--lighten-1">mdi-discord</v-icon>
                      </a>
                    </template>
                    <span>{{ member.discord }}</span>
                  </v-tooltip>
                </div>
            </v-card>
          </v-col>
        </v-row>
        <p class="pa-5 mt-10 text-h5 font-weight-medium text-uppercase text-center">Business Development Team</p>
          <v-row>
            <v-col cols="12" sm="12" md="4" v-for="(member, index) in business" :key="index">
              <v-card width="250" class="rounded-xl mx-auto">
                  <div class="text-center">
                    <v-avatar size="120" class="mt-5">
                      <v-img :src="member.get_image"></v-img>
                    </v-avatar>
                  </div>
                  <span class="text-h5 text-center font-weight-bold d-block mt-5">{{ member.name }}</span>
                  <span class="text-center d-block">{{ member.title }}</span>
                  <div class="d-flex justify-space-around pa-5">
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on, attrs }">
                        <a @click="mailTo(member.email)" v-bind="attrs" v-on="on" style="text-decoration:none; color:white">
                          <v-icon size="25" class="text--lighten-1">mdi-gmail</v-icon>
                        </a>
                      </template>
                      <span>{{ member.email }}</span>
                    </v-tooltip>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on, attrs }">
                        <a :href="member.linkedin" v-bind="attrs" v-on="on" target="_blank" style="text-decoration:none; color:white">
                          <v-icon size="25" class="text--lighten-1">mdi-linkedin</v-icon>
                        </a>
                      </template>
                      <span>{{ member.linkedin }}</span>
                    </v-tooltip>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on, attrs }">
                        <a :href="member.portfolio" v-bind="attrs" v-on="on" target="_blank" style="text-decoration:none; color:white">
                          <v-icon size="25" class="text--lighten-1">mdi-web</v-icon>
                        </a>
                      </template>
                      <span>{{ member.portfolio }}</span>
                    </v-tooltip>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on, attrs }">
                        <a :href="member.github" v-bind="attrs" v-on="on" target="_blank" style="text-decoration:none; color:white">
                          <v-icon size="25" class="text--lighten-1">mdi-github</v-icon>
                        </a>
                      </template>
                      <span>{{ member.github }}</span>
                    </v-tooltip>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on, attrs }">
                        <a href="#" v-bind="attrs" v-on="on" style="text-decoration:none; color:white">
                          <v-icon size="25" class="text--lighten-1">mdi-discord</v-icon>
                        </a>
                      </template>
                      <span>{{ member.discord }}</span>
                    </v-tooltip>
                  </div>
              </v-card>
            </v-col>
          </v-row>
      </v-container>
    </div>
</template>

<script>
import axios from 'axios'

// components
import Spinner from '@/components/Spinner.vue'

export default {
  components: { Spinner },
  metaInfo: {
    
  },
  data(){
    return{
      members:[],
    }
  },
   created(){
    this.getData();
  },

  methods:{
    mailTo(param){
      window.location.href = 'mailto:' + param;
    },
    async getData(){
      try {
        const results = await axios.get('http://127.0.0.1:8000/api/team')
        this.members = results.data
      } catch (error) {
        console.log(error)
      }
    }
  },
  computed:{
    core: function(){
      return this.members.filter( d=> d.
        team_type === "core")
    },
    business: function(){
      return this.members.filter( d=> d.
        team_type === "business")
    }
  },
}
</script>

<style>

</style>
