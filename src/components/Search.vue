<template>
  <div class="search">
    <div>
      <input
        type="search"
        name="search"
        id="search"
        placeholder="Search by weapon name&hellip;"
        :disabled="!(items && items.length > 0)"
        @input="runSearch"
      >
    </div>
    <div>
      <select
        name="items"
        id="items"
        :disabled="!(items && items.length > 0)"
        @change="selectItem"
      >
        <option
          v-for="(item, key) in items"
          :key="key"
          :value="item.value"
        >
          {{ item.label }}
        </option>
      </select>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  items: {
    type: Object,
    required: false,
  },
})

const emit = defineEmits(['search', 'pick-category'])

const runSearch = (ev: Event) => {
  const output = (ev.currentTarget as HTMLInputElement).value
  emit('search', output)
}

const selectItem = (ev: Event) => {
  const output = (ev.currentTarget as HTMLInputElement).value
  emit('pick-category', output)
}
</script>

<style scoped>
.search {
  @apply 
    xl:flex
    xl:items-center
    xl:gap-4
    mb-4;
}

.search > div {
  @apply xl:flex xl:items-stretch xl:flex-1;
}

.search input[type="search"],
.search select {
  @apply
    block
    h-14
    w-full
    p-4
    m-0
    bg-amber-200
    rounded-md
    border-0
    outline-0
    text-black
    placeholder:text-black
    placeholder:italic;
}
</style>
