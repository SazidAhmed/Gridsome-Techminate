<template>
    <div>
      <v-container >
        <p class="pa-5 mt-10 text-h3 font-weight-medium text-uppercase text-center">Core Team</p>
        <v-row>
          <v-col cols="12" sm="12" md="4" v-for="(service, index) in core" :key="index">
            <v-card width="250" class="rounded-xl mx-auto">
                <div class="text-center">
                  <v-avatar size="100" class="mt-5">
                    <v-icon size="90" class="text--lighten-1">mdi-account-tie</v-icon>
                  </v-avatar>
                </div>
                <span class="text-h5 text-center font-weight-bold d-block mt-5">{{ service.name }}</span>
                <span class="text-center d-block">{{ service.designation }}</span>
                <div class="d-flex justify-space-around pa-5">
                    <v-icon size="25" class="text--lighten-1">mdi-gmail</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-linkedin</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-web</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-github</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-discord</v-icon>
                </div>
            </v-card>
          </v-col>
        </v-row>
        <p class="pa-5 mt-10 text-h3 font-weight-medium text-uppercase text-center">Business Development Team</p>
        <v-row>
          <v-col cols="12" sm="12" md="3" lg="2" v-for="(service, index) in services" :key="index">
            <v-card width="250" class="rounded-xl mx-auto">
                <div class="text-center">
                  <v-avatar size="100" class="mt-5">
                    <v-icon size="90" class="text--lighten-1">mdi-account-tie</v-icon>
                  </v-avatar>
                </div>
                <span class="text-h5 text-center font-weight-bold d-block mt-5">{{ service.name }}</span>
                <span class="text-center d-block">{{ service.designation }}</span>
                <div class="d-flex justify-space-around pa-5">
                    <v-icon size="25" class="text--lighten-1">mdi-gmail</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-linkedin</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-web</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-github</v-icon>
                    <v-icon size="25" class="text--lighten-1">mdi-discord</v-icon>
                </div>
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
      core:[
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
      ],
       services:[
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
        {"name":"Sazid Ahmed","designation":"Software Engineer", "linkedin":"", "github":"", "email":"sazidahmed.official@gmail.com"},
      ]
    }
  }
}
</script>

<style>

</style>
