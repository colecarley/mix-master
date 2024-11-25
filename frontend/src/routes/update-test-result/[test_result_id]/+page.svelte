<script lang="ts">
    import { page } from "$app/stores";
    import type { TestResult } from "$lib/entities/test-results";
    import TestResultEntityInstance from "$lib/entities/test-results";
    import { onMount } from "svelte";
    import Center from "../../../components/center.svelte";
    import Header from "../../../components/header.svelte";
    import Squeeze from "../../../components/squeeze.svelte";
    import TestResultForm from "../../../components/test-result-form.svelte";

    let testResult: TestResult | null = $state(null);
    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { test_result_id } = value.params;

            testResult = await TestResultEntityInstance.get(
                Number(test_result_id),
            );
        });

        sub();
    });
</script>

<Center>
    <Header></Header>
    <Squeeze>
        <h1 class="mb-6 text-gray-600">Update Test Result</h1>
        {#if testResult}
            <TestResultForm form={testResult} testResultId={testResult.id}
            ></TestResultForm>
        {/if}
    </Squeeze>
</Center>
