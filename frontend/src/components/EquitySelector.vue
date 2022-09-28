<template>

<select name="equity" id="eq">
    <v-select
          :options="options"
          :value="equity.name"
          @input="(country) => updateCountry(person, country)"
        />
</select>
<button></button>
</template>

<script>
import axios from 'axios';
export default {
    name: "EquitySelector",
    created() {
        axios.get("http://localhost:8000/equities")
        .then(res=>{
            console.log(res);
            this.equities = equity
        });
    },
}
</script>

<style></style>