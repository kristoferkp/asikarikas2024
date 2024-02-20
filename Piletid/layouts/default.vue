<template>
	<div class="bg-white dark:bg-gray-800 min-h-screen">
		<div class="flex flex-col h-screen">
			<div class="sticky top-0 z-50"><Navbar /></div>
			<div class="grow"><slot /></div>
			<div class="sticky bottom-0 z-50"><Footer /></div>
		</div>
	</div>
</template>
