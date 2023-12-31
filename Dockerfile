FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["hello.csproj", "MyWebApp/"]
COPY ["hello.cs", "MyWebApp/"]
RUN dotnet restore "MyWebApp/hello.csproj"
COPY . .
WORKDIR "/src/MyWebApp"
RUN dotnet build "hello.csproj" -c Release -o /app/build
FROM build AS publish
RUN dotnet publish "hello.csproj" -c Release -o /app/publish
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "hello.dll"]
