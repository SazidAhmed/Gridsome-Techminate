<template>
    <div>
      <v-container >
        <p class="pa-5 mt-10 text-h3 font-weight-medium text-uppercase text-center">Our Services</p>
        <v-row>
          <v-col cols="12" sm="12" md="4" v-for="(service, index) in services" :key="index">
            <v-card width="400" class="rounded-xl mx-auto">
                <div class="d-flex justify-space-around pt-10">
                    <v-avatar size="95" class="d-inline">
                        <svg class="w-6 h-6 blue--text text--darken-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                    </v-avatar>
                    <p class="grey--text text--lighten-3 text-h1 font-weight-bold d-inline">{{ service.number }}</p>
                </div>
                <p class="text-h5 text-center font-weight-bold mt-5">{{ service.title }}</p>
                <p class="font-weight-medium ml-10 mr-10 pb-8">
                  {{ service.description }}
                </p>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
</template>

<script>
export default {
  metaInfo: {
    
  },
  data(){
    return{
      services:[
        {"title":"Software Development","icon":"icon", "number":"01", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Website Development","icon":"icon", "number":"02", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"UI/UX Design","icon":"icon", "number":"03", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Cloud & DevOps","icon":"icon", "number":"04", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Analytic Solutions","icon":"icon", "number":"05", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"},
        {"title":"Database Administration","icon":"icon", "number":"06", "description":"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Non, quis. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatum, tenetur!"}
      ]
    }
  }
}
</script>

<style>

</style>
