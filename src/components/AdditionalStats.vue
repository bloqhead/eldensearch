<template>
  <div class="additional-stats" v-if="weapon.additional_stats">
    <button 
      @click="toggleExpanded" 
      class="drawer-toggle"
      :class="{ 'expanded': isExpanded }"
    >
      <span>Additional Stats</span>
      <fa :icon="['fas', isExpanded ? 'chevron-up' : 'chevron-down']" />
    </button>
    
    <div v-if="isExpanded" class="drawer-content">
      <!-- Status Effects -->
      <div class="status-effects" v-if="hasStatusEffects">
        <h5 class="subsection-title">Status Effects</h5>
        <div class="status-grid">
          <div v-if="weapon.additional_stats.blood_loss > 0" class="status-item">
            <span class="status-label">Blood Loss</span>
            <span class="status-value">{{ weapon.additional_stats.blood_loss }}</span>
          </div>
          <div v-if="weapon.additional_stats.frost > 0" class="status-item">
            <span class="status-label">Frost</span>
            <span class="status-value">{{ weapon.additional_stats.frost }}</span>
          </div>
          <div v-if="weapon.additional_stats.poison > 0" class="status-item">
            <span class="status-label">Poison</span>
            <span class="status-value">{{ weapon.additional_stats.poison }}</span>
          </div>
          <div v-if="weapon.additional_stats.scarlet_rot > 0" class="status-item">
            <span class="status-label">Scarlet Rot</span>
            <span class="status-value">{{ weapon.additional_stats.scarlet_rot }}</span>
          </div>
          <div v-if="weapon.additional_stats.sleep > 0" class="status-item">
            <span class="status-label">Sleep</span>
            <span class="status-value">{{ weapon.additional_stats.sleep }}</span>
          </div>
          <div v-if="weapon.additional_stats.madness > 0" class="status-item">
            <span class="status-label">Madness</span>
            <span class="status-value">{{ weapon.additional_stats.madness }}</span>
          </div>
        </div>
      </div>

      <!-- Weapon Properties -->
      <div class="weapon-properties">
        <h5 class="subsection-title">Weapon Properties</h5>
        <div class="properties-grid">
          <div class="property-item">
            <span class="property-label">Range</span>
            <span class="property-value">{{ weapon.additional_stats.range }}</span>
          </div>
          <div class="property-item">
            <span class="property-label">Attack Speed</span>
            <span class="property-value">{{ weapon.additional_stats.attack_speed }}</span>
          </div>
          <div class="property-item">
            <span class="property-label">Stamina Cost</span>
            <span class="property-value">{{ weapon.additional_stats.stamina_cost }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Weapon } from '../types'

interface Props {
  weapon: Weapon
}

const props = defineProps<Props>()

const isExpanded = ref(false)

const toggleExpanded = () => {
  isExpanded.value = !isExpanded.value
}

const hasStatusEffects = computed(() => {
  if (!props.weapon.additional_stats) return false
  const stats = props.weapon.additional_stats
  return stats.blood_loss > 0 || stats.frost > 0 || stats.poison > 0 || 
         stats.scarlet_rot > 0 || stats.sleep > 0 || stats.madness > 0
})
</script>

<style scoped>
.additional-stats {
  @apply
    border
    border-slate-600
    rounded-lg
    overflow-hidden
    mt-4;
}

.drawer-toggle {
  @apply
    w-full
    px-4
    py-3
    bg-slate-700
    hover:bg-slate-600
    transition-colors
    flex
    justify-between
    items-center
    text-left
    font-medium
    text-slate-300
    cursor-pointer;
}

.drawer-toggle.expanded {
  @apply bg-slate-600;
}

.drawer-content {
  @apply
    p-4
    bg-slate-750
    space-y-4;
}

.subsection-title {
  @apply
    text-sm
    font-medium
    text-slate-300
    mb-2;
}

.status-grid {
  @apply
    grid
    grid-cols-2
    gap-2;
}

.status-item {
  @apply
    bg-slate-700
    rounded-lg
    p-2
    flex
    justify-between
    items-center
    border
    border-slate-600;
}

.status-label {
  @apply
    text-xs
    text-slate-400
    font-medium;
}

.status-value {
  @apply
    text-emerald-400
    font-mono
    text-sm
    font-semibold;
}

.properties-grid {
  @apply
    grid
    gap-2;
}

.property-item {
  @apply
    bg-slate-700
    rounded-lg
    p-2
    flex
    justify-between
    items-center
    border
    border-slate-600;
}

.property-label {
  @apply
    text-xs
    text-slate-400
    font-medium;
}

.property-value {
  @apply
    text-emerald-400
    font-mono
    text-sm
    font-semibold;
}
</style>