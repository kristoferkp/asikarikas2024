<template>
    <div>
        <ul>
            <li v-for="purchase in data" :key="purchase.purchase_id">
                {{ purchase.purchase_id }} - {{ purchase.tickt_id }} - {{ purchase.user_id }} - {{ purchase.purchase_date }}
            </li>
        </ul>
    </div>
</template>

<script setup>
	const supabase = useSupabaseClient();

	const { data } = await supabase
        .from('purchases')
        .select()
</script>