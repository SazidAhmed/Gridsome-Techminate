<template>
  <div>
      <!-- parent relative child absolute -->
      <v-container fluid class="bg">
        <v-row no-gutters class="pa-12">
          <v-col cols="12" sm="12" md="1" lg="1">
          </v-col>
          <v-col cols="12" sm="12" md="4" lg="4">
            <div class="pa-10 white--text text-uppercase">
              <p class="font-weight-medium text-h5">Our Workflow</p>
              <p class="font-weight-medium mt-10">We follow these steps to process a project and handover to our clients</p>
            </div>
          </v-col>
          <v-col cols="12" sm="12" md="6" lg="6">
            <v-row>
              <v-col cols="12" sm="6" md="6" v-for="(service, index) in data" :key="index">
                <v-card width="400" style="background: #FC5108; border-radius: 0px 80px;">
                    <div class="d-flex justify-space-around pt-10">
                      <v-avatar :color="service.color" size="60">
                        <span class="white--text headline">{{ service.number }}</span>
                      </v-avatar>
                    </div>
                    <p class="text-h5 text-center font-weight-bold mt-5">{{ service.title }}</p>
                    <p class="font-weight-medium ml-10 mr-10 pb-8">
                      {{ service.description }}
                    </p>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
  </div>
</template>

<script>
export default {
  metaInfo: {
    title: 'Home'
  },
  data(){
    return{
      data:[
        {"title":"Analysis","color":"purple", "number":"1", "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."},
        {"title":"Planning","color":"green", "number":"2", "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."},
        {"title":"Execute","color":"lime", "number":"3", "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."},
        {"title":"Deliver","color":"blue", "number":"4", "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit."},
      ]
    }
  }
}
</script>

<style scoped>
.bg{
background: linear-gradient(90deg, #FC575E 0%, #F7B42C 100%), #C4C4C4;
border-radius: 0px 300px 3px;
}
</style>
