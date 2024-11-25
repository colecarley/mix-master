<script lang="ts">
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import Squeeze from "../../components/squeeze.svelte";
    import TestResultForm from "../../components/test-result-form.svelte";
</script>

<Header></Header>
<Center>
    <Squeeze>
        <TestResultForm testResultId={null}></TestResultForm>
    </Squeeze>
</Center>
