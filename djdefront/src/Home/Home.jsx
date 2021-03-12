/* import withRoot from "./modules/withRoot"; */
// --- Post bootstrap -----
import React from "react";
/* import ProductCategories from "./modules/views/ProductCategories";
import ProductSmokingHero from "./modules/views/ProductSmokingHero";
import AppFooter from "./modules/views/AppFooter";*/
import Apresentacao from "../components/Apresentacao";
/* import ProductValues from "./modules/views/ProductValues";
import ProductHowItWorks from "./modules/views/ProductHowItWorks";
import ProductCTA from "./modules/views/ProductCTA";  */
import Navbar from "../components/Navbar";

function Index() {
  return (
    <React.Fragment>
      <Navbar />
      <Apresentacao />
      {/*
      <ProductValues />
      <ProductCategories />
      <ProductHowItWorks />
      <ProductCTA />
      <ProductSmokingHero />
      <AppFooter /> */}
    </React.Fragment>
  );
}

/* export default withRoot(Index); */
export default Index;
