<template>
  <div class="search">
    <div>
      <label for="search">
        Search
      </label>
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
      <label for="categories">
        Category
      </label>
      <select
        name="categories"
        id="categories"
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

const emit = defineEmits([
  'search',
  'pick-category',
])

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
    flex
    flex-col
    sm:flex-row
    items-center
    gap-2
    md:gap-4;
}

.search > div {
  @apply
    flex
    flex-col
    gap-2
    md:flex-1
    w-full
    md:w-auto;
}

.search label {
  @apply
    flex
    items-center
    gap-2
    font-serif
    text-sm
    text-slate-500
    font-thin
    tracking-widest
    uppercase
    after:block
    after:flex-1
    after:h-[1px]
    after:bg-slate-500;
}
</style>
