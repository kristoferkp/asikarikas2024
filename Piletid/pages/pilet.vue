<template>
	<div class="max-w-6xl mx-auto">
		<h1 class="text-4xl font-semibold text-gray-800 dark:text-gray-200">
			Pileti info
		</h1>
		<!-- Table Section -->
		<div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
			<!-- Card -->
			<div class="flex flex-col">
				<div class="-m-1.5 overflow-x-auto">
					<div class="p-1.5 min-w-full inline-block align-middle">
						<div
							class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden dark:bg-slate-900 dark:border-gray-700">
							<!-- Table -->
							<table
								class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
								<thead
									class="bg-gray-50 divide-y divide-gray-200 dark:bg-gray-800 dark:divide-gray-700">
									<tr>
										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
												Lähtepeatus
											</span>
										</th>
										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
												Sihtpeatus
											</span>
										</th>
										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
												Stardi aeg
											</span>
										</th>

										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
												Kohalejõudmise aeg
											</span>
										</th>

										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
												Kuupäev
											</span>
										</th>

										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
												Transpordivahend
											</span>
										</th>

										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
												Hind
											</span>
										</th>
										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											</span>
										</th>
										<th scope="col" class="px-6 py-3 text-start">
											<span
												class="text-xs font-semibold uppercase tracking-wide text-gray-800 dark:text-gray-200">
											</span>
										</th>
									</tr>
								</thead>

								<tbody class="divide-y divide-gray-200 dark:divide-gray-700">
									<tr>
										<td class="h-px w-auto whitespace-nowrap">
											<div class="px-6 py-2 flex items-center gap-x-3">
												<span class="text-sm text-gray-600 dark:text-gray-400">
													{{ ticket?.from }}
												</span>
											</div>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<div class="px-6 py-2 flex items-center gap-x-3">
												<span
													class="font-semibold text-sm text-gray-600 dark:text-gray-400">
													{{ ticket?.to }}
												</span>
											</div>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<div class="px-6 py-2 flex items-center gap-x-3">
												<span
													class="font-semibold text-sm text-gray-600 dark:text-gray-400">
													{{ ticket?.start_time }}
												</span>
											</div>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<div class="px-6 py-2">
												<span
													class="text-sm text-gray-800 dark:text-gray-200"
													>{{ ticket?.end_time }}</span
												>
											</div>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<div class="px-6 py-2 flex items-center gap-x-3">
												<span class="text-sm text-gray-600 dark:text-gray-400">
													{{ ticket?.date }}
												</span>
											</div>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<div class="px-6 py-2">
												<span
													class="text-sm text-gray-800 dark:text-gray-200"
													>{{ ticket?.vehicle_type }}</span
												>
											</div>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<div class="px-6 py-2">
												<span
													class="font-semibold text-sm text-gray-800 dark:text-gray-200"
													>{{ ticket?.price }}€</span
												>
											</div>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<button
												type="button"
												class="hs-collapse-toggle max-w-sm m-1 py-2 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-gradient-to-tl from-blue-600 to-violet-600 hover:from-violet-600 hover:to-blue-600 text-white disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
												id="hs-basic-collapse"
												data-hs-collapse="#hs-basic-collapse-heading">
												Peatused
												<svg
													class="hs-collapse-open:rotate-180 flex-shrink-0 size-4 text-white"
													xmlns="http://www.w3.org/2000/svg"
													width="24"
													height="24"
													viewBox="0 0 24 24"
													fill="none"
													stroke="currentColor"
													stroke-width="2"
													stroke-linecap="round"
													stroke-linejoin="round">
													<path d="m6 9 6 6 6-6" />
												</svg>
											</button>
										</td>
										<td class="h-px w-auto whitespace-nowrap">
											<button
												@click="buy(ticket)"
												class="max-w-sm m-1 py-2 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-gradient-to-tl from-blue-600 to-violet-600 hover:from-violet-600 hover:to-blue-600 text-white disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
												Osta
											</button>
										</td>
									</tr>
								</tbody>
							</table>
							<!-- End Table -->
						</div>
					</div>
				</div>
			</div>
			<!-- End Card -->
		</div>
		<!-- End Table Section -->
		<div
			id="hs-basic-collapse-heading"
			class="hs-collapse hidden w-full overflow-hidden transition-[height] duration-300"
			aria-labelledby="hs-basic-collapse">
            <h3 class="text-xl font-semibold text-gray-800 dark:text-gray-200">Peatused: </h3>
			<ul v-for="stop in ticket?.stops" class="mt-5">
				<li class="text-gray-500 dark:text-gray-400">
					- {{ stop }}
                </li>
			</ul>
		</div>
	</div>
</template>

<script setup>
	import { getData, setData } from "nuxt-storage/local-storage";
	const ticket = getData("ticket");
	console.log(ticket);

	const supabase = useSupabaseClient();
	async function buy(ticket) {
		const user = supabase.auth.getUser();
		const email = getData("email");

		if (!user) {
			alert("Logi sisse, et osta pilet ning siduda pilet kontoga");
			return;
		}
		if (confirm("Kas oled kindel, et soovid pileti osta?") == true) {
			const { data, error } = await supabase.from("purchases").insert([
				{
					ticket_id: ticket.ticket_id,
				},
			]);
			if (error) {
				alert("Viga pileti ostmisel");
			} else {
				await supabase.auth.resetPasswordForEmail(email);
				alert("Pilet ostetud");
			}
		}
	}
</script>
