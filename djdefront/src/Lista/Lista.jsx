import React, { PureComponent } from "react";

class Lista extends PureComponent {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <>
        <div id="myCarousel" className="carousel slide" data-ride="carousel">
          <ol className="carousel-indicators">
            <li
              data-target="#myCarousel"
              data-slide-to="0"
              className="active"
            ></li>
            <li data-target="#myCarousel" data-slide-to="1"></li>
            <li data-target="#myCarousel" data-slide-to="2"></li>
          </ol>
          <div className="carousel-inner">
            <div className="carousel-item active">
              <img
                className="capaprincipal"
                src="../../static/assets/home.jpg"
                width="500px"
                height="300px"
              />
              <div className="container">
                <div className="carousel-caption text-left">
                  <h1>Como são as aulas?</h1>
                  <p>
                    Você escolhe onde e como estudar e ainda pode contar* com a
                    ajuda de nosso time.
                  </p>
                  <p>
                    <a
                      className="btn btn-lg btn-primary"
                      href="/atividadesgratis"
                      role="button"
                    >
                      Comece agora grátis
                    </a>
                  </p>
                  <p style={{ fontSize: "12px" }}>*Clique aqui e saiba mais</p>
                </div>
              </div>
            </div>
            <div className="carousel-item">
              <img
                className="capa2"
                src="../../static/assets/capa2.jpg"
                width="500px"
                height="800px"
              />
              <div className="container">
                <div className="carousel-caption">
                  <h1>Que materiais você precisa?</h1>
                  <p>Celular, computador ou tablet.</p>
                  <p>
                    <a
                      className="btn btn-lg btn-primary"
                      href="#"
                      role="button"
                    >
                      Saber mais
                    </a>
                  </p>
                </div>
              </div>
            </div>
            <div className="carousel-item">
              <img
                className="capa3"
                src="../../static/assets/equipe.jpg"
                width="500px"
                height="800px"
              />
              <div className="container">
                <div className="carousel-caption text-right">
                  <h1>O melhor time de professores do Brasil.</h1>
                  <p>
                    Todos pesquisadores formados pelas melhores universidades do
                    Rio de Janeiro e com vasta experiência no ensino de
                    Matemática.
                  </p>
                  <p>
                    <a
                      className="btn btn-lg btn-primary"
                      href="#"
                      role="button"
                    >
                      Ver time
                    </a>
                  </p>
                </div>
              </div>
            </div>
          </div>
          <a
            className="carousel-control-prev"
            href="#myCarousel"
            role="button"
            data-slide="prev"
          >
            <span
              className="carousel-control-prev-icon"
              aria-hidden="true"
            ></span>
            <span className="sr-only">Previous</span>
          </a>
          <a
            className="carousel-control-next"
            href="#myCarousel"
            role="button"
            data-slide="next"
          >
            <span
              className="carousel-control-next-icon"
              aria-hidden="true"
            ></span>
            <span className="sr-only">Next</span>
          </a>
        </div>

        <div className="container marketing">
          <div className="row">
            <div className="col-lg-4">
              <img
                src="../../static/assets/logo.png"
                width="140px"
                height="140px"
              />
              {/*  <svg
                className="bd-placeholder-img rounded-circle"
                width="140"
                height="140"
                xmlns="http://www.w3.org/2000/svg"
                preserveAspectRatio="xMidYMid slice"
                focusable="false"
                role="img"
                aria-label="Placeholder: 140x140"
              >
                <title>Placeholder</title>
                <rect width="100%" height="100%" fill="#777" />
                <text x="50%" y="50%" fill="#777" dy=".3em">140x140</text>
              </svg> */}
              <h2>Quem somos</h2>
              <p>Projeto de Desenvolvimento de Jogos Digitais na Educação</p>
              <p>
                <a
                  className="btn btn-secondary"
                  href="https://jogosdigitais.cap.ufrj.br/home"
                  role="button"
                >
                  Página do Projeto DJDE &raquo;
                </a>
              </p>
            </div>
            <div className="col-lg-4">
              <img
                className="rounded-circle"
                src="../../static/assets/depoimentos.png"
                width="140px"
                height="140px"
              />
              {/* <svg
                className="bd-placeholder-img rounded-circle"
                width="140"
                height="140"
                xmlns="http://www.w3.org/2000/svg"
                preserveAspectRatio="xMidYMid slice"
                focusable="false"
                role="img"
                aria-label="Placeholder: 140x140"
              >
                <title>Placeholder</title>
                <rect width="100%" height="100%" fill="#777" />
                <text x="50%" y="50%" fill="#777" dy=".3em">140x140</text>
              </svg> */}
              <h2>Depoimentos</h2>
              <p>Professor Marcos Monte: O GeniAulas mudou minha vida!</p>
              <p>
                <a className="btn btn-secondary" href="#" role="button">
                  Ver detalhes &raquo;
                </a>
              </p>
            </div>
            <div className="col-lg-4">
              <img
                className="rounded-circle"
                src="../../static/assets/escola.jpeg"
                width="140px"
                height="140px"
              />
              {/*  <svg
                className="bd-placeholder-img rounded-circle"
                width="140"
                height="140"
                xmlns="http://www.w3.org/2000/svg"
                preserveAspectRatio="xMidYMid slice"
                focusable="false"
                role="img"
                aria-label="Placeholder: 140x140"
              >
                <title>Placeholder</title>
                <rect width="100%" height="100%" fill="#777" />
                <text x="50%" y="50%" fill="#777" dy=".3em">140x140</text>
              </svg>  */}
              <h2>Escolas parceiras</h2>
              <p>Escola Alemã Corcovado, CAP/UFRJ, CIEP 098</p>
              <p>
                <a className="btn btn-secondary" href="#" role="button">
                  Ver mais &raquo;
                </a>
              </p>
            </div>
          </div>

          <hr className="featurette-divider" />

          <div className="row featurette">
            <div className="col-md-7">
              <h2 className="featurette-heading">
                Por que escolher o GeniAulas?
              </h2>
              <p className="lead">
                Junte-se a 4 milhões de estudantes tirando notas 2x mais altas
              </p>
            </div>
            <div className="col-md-5">
              <img
                src="../../static/assets/porque.png"
                width="500px"
                height="500px"
              />
              {/* <svg
                className="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"
                width="500"
                height="500"
                xmlns="http://www.w3.org/2000/svg"
                preserveAspectRatio="xMidYMid slice"
                focusable="false"
                role="img"
                aria-label="Placeholder: 500x500"
              >
                <title>Placeholder</title>
                <rect width="100%" height="100%" fill="#eee" />
                <text x="50%" y="50%" fill="#aaa" dy=".3em">500x500</text>
              </svg> */}
            </div>
          </div>

          <hr className="featurette-divider" />

          <div className="row featurette">
            <div className="col-md-7 order-md-2">
              <h2 className="featurette-heading">
                <span className="text-muted">Venha para o sucesso</span>
              </h2>
              <p className="lead">
                Não importa se está estudando de casa ou se já voltou à escola.
                Nossos materiais gratuitos, interativos e personalizados vão te
                ajudar a aprender melhor.
              </p>
            </div>
            <div className="col-md-5 order-md-1">
              <img
                src="../../static/assets/materiais.png"
                width="450px"
                height="450px"
              />
              {/*  <svg
                className="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"
                width="500"
                height="500"
                xmlns="http://www.w3.org/2000/svg"
                preserveAspectRatio="xMidYMid slice"
                focusable="false"
                role="img"
                aria-label="Placeholder: 500x500"
              >
                <title>Placeholder</title>
                <rect width="100%" height="100%" fill="#eee" />
                <text x="50%" y="50%" fill="#aaa" dy=".3em">500x500</text>
              </svg>  */}
            </div>
          </div>

          <hr className="featurette-divider" />

          <div className="row featurette">
            <div className="col-md-7">
              <h2 className="featurette-heading">Aprenda 2x mais rápido</h2>
              <p className="lead">
                A metodologia GeniAulas foi desenvolvida por neurocientistas e
                educadores de Oxford e outros centros acadêmicos para te ajudar
                a aprender melhor e mais rápido. Nós focamos em exercícios e
                atividades para você estudar de forma mais dinâmica, divertida e
                eficiente.
              </p>
            </div>
            <div className="col-md-5">
              <img
                src="../../static/assets/tecnica.jpeg"
                width="500px"
                height="500px"
              />

              {/*  <svg
                className="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto"
                width="500"
                height="500"
                xmlns="http://www.w3.org/2000/svg"
                preserveAspectRatio="xMidYMid slice"
                focusable="false"
                role="img"
                aria-label="Placeholder: 500x500"
              >
                <title>Placeholder</title>
                <rect width="100%" height="100%" fill="#eee" />
                <text x="50%" y="50%" fill="#aaa" dy=".3em">500x500</text>
              </svg>  */}
            </div>
          </div>

          <hr className="featurette-divider" />
        </div>

        {/*     
                   <td>{{ estudante.pk }}</td>
              <td>{{ estudante.nome_completo }}</td>
              <td>{{ estudante.email }}</td>
              <td>{{ estudante.senha }}</td>
              <td>{{ estudante.telefone }}</td>
              <td>{{ estudante.cpf_responsavel }}</td>
              <td>{{ estudante.data_de_nascimento }}</td>
              <td>{{ estudante.ano_de_escolaridade }}</td>
              <td>{{ estudante.instituicao }}</td>
              <td>{{ estudante.cidade }}</td>
              <td>{{ estudante.estado }}</td>
              <td>{{ estudante.foto }}</td>
              <td>{{ estudante.created_date }}</td>
              <td>{{ estudante.updated_date }}</td> */}
      </>
    );
  }
}

export default Lista;
