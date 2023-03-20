<template>
  <div class="list">
    <ul
      v-if="items && items.length > 0"
      class="list-items"
    >
      <li
        v-for="(item, idx) in items"
        :key="item.id"
        :data-index="idx"
        :style="`--i: ${idx}`"
      >
        <header>
          <h3 class="title">
            {{ item.weapon }}
          </h3>
          <span
            v-if="item.tier"
            class="tier"
          >
            {{ item.tier }}
          </span>
        </header>
        <div
          v-if="item.scaling && item.scaling.length > 0"
          class="scaling"
        >
          <h4 class="section-title">
            Scaling
          </h4>
          <ul>
            <li
              v-for="(scale, idx2) in item.scaling"
              :key="idx2"
            >
              <template
                v-for="(value, name) in scale"
                :key="name"
              >
                <h5 class="scaling-label">
                  {{ name }}
                </h5>
                <p class="scaling-value">
                  {{ value }}
                </p>
              </template>
            </li>
          </ul>
        </div>
        <div>
          <h4 class="section-title">
            Stats
          </h4>
          <div class="stats">
            <ul>
              <li
                v-for="(value, stat) in item.stats"
                :key="stat"
                :title="stat"
                class="stat"
              >
                <span>
                  <fa
                    v-if="iconHandler(stat).length > 0"
                    :icon="iconHandler(stat)"
                  />
                </span>
                <span>
                  {{ value }}
                </span>
              </li>
            </ul>
          </div>
        </div>
      </li>
    </ul>
    <div v-else>
      <p>No items found.</p>
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

const iconHandler = (name: String | Number) => {
  let icon: String | Number = name !== undefined ? name : ''!

  switch(name.toString().toLowerCase()) {
    case 'weight' :
      icon = 'weight-hanging'
      break
    case 'physical' :
      icon = 'sword'
      break
    case 'magic' :
      icon = 'wand-magic-sparkles'
      break
    case 'fire' : 
      icon = 'fire'
      break
    case 'light' :
      icon = 'lightbulb'
      break
    case 'holy' :
      icon = 'book-bible'
      break
    default :
      icon = ''
  }

  return ['fasr', icon]
}
</script>

<style scoped>
.list {

}

.list-items {
  @apply
    flex
    flex-col
    gap-4
    md:grid
    md:grid-cols-2
    lg:grid-cols-3;
}

.title {
  @apply
    text-xl
    md:text-2xl;
}

.list-items header {
  @apply
    flex
    justify-between
    items-center
    px-6
    py-2
    mb-2
    -mt-4
    -ml-4
    -mr-4
    md:-mt-6
    md:-ml-6
    md:-mr-6
    bg-slate-700;
}

.tier {
  @apply
    font-serif
    text-xl
    bg-slate-800
    text-emerald-500
    px-3
    py-1
    rounded-md;
}

.list-items > li {
  @apply
    p-4
    md:p-6
    bg-slate-800;
}

.scaling > ul {
  @apply
    w-full
    grid
    grid-flow-col
    auto-cols-fr
    items-center
    justify-center
    gap-4
    divide-x
    divide-slate-500
    text-center;
}

.scaling > ul > li {
  @apply p-2;
}

.scaling-label {
  @apply
    uppercase
    text-sm;
}

.scaling-value {
  @apply
    uppercase
    text-3xl
    font-serif
    text-emerald-500;
}

.section-title {
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
    my-2
    after:block
    after:flex-1
    after:h-[1px]
    after:bg-slate-500;
}

.stats > ul {
  @apply
    grid
    grid-cols-3
    gap-2
    text-center;
}

.stats > ul > li {
  @apply
    bg-slate-700
    rounded-lg
    flex
    items-center
    justify-center
    border-2
    border-slate-800;
}

.stats > ul > li span {
  @apply
    flex-1
    p-2
    first:border-r-2
    first:border-slate-800
    first:text-emerald-500
    last:font-mono;
}
</style>