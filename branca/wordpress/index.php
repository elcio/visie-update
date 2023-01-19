<?php get_header(); ?>

<?php
wp_nav_menu();
if ( have_posts() ) :
    while ( have_posts() ) :
        the_post();
        ?>
        <hr />
        <h1><?php the_title(); ?></h1>
        <?php the_content(); ?>
        <?php
    endwhile;
endif;
?>

<?php get_footer(); ?>
