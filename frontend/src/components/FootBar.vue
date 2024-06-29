<template>
    <div class="position-fixed bottom-0 w-100 bg-dark special-footer p-2">
        <div class="text-center text-white footer-title">Footer</div>
    </div>
</template>

<style>
    .special-footer{
        height: 50px;
        transition: height 1s;
    }

    .special-footer:hover{
        height: 250px;
        & .footer-title{
            display: none;
        }
    }
</style>